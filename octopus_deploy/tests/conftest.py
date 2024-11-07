# (C) Datadog, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import json
import os
from pathlib import Path
from urllib.parse import urlparse

import mock
import pytest
import requests

from datadog_checks.dev import docker_run
from datadog_checks.dev.conditions import CheckDockerLogs, CheckEndpoints
from datadog_checks.dev.fs import get_here

from .constants import COMPOSE_FILE, INSTANCE, LAB_INSTANCE, USE_OCTOPUS_LAB


@pytest.fixture(scope='session')
def dd_environment():
    if USE_OCTOPUS_LAB:
        yield LAB_INSTANCE
    else:
        compose_file = COMPOSE_FILE
        endpoint = INSTANCE["octopus_endpoint"]
        conditions = [
            CheckDockerLogs(identifier='octopus-api', patterns=['server running']),
            CheckEndpoints(f'{endpoint}/spaces'),
        ]
        with docker_run(compose_file, conditions=conditions):
            yield INSTANCE


@pytest.fixture
def instance():
    return {'octopus_endpoint': 'http://localhost:80/api', 'space': 'Default'}


def get_json_value_from_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def get_url_path(url):
    parsed_url = urlparse(url)
    return parsed_url.path + "?" + parsed_url.query if parsed_url.query else parsed_url.path


@pytest.fixture
def mock_responses():
    responses_map = {}

    def process_files(dir, response_parent):
        for file in dir.rglob('*'):
            if file.is_file() and file.stem != ".slash":
                relative_dir_path = (
                    "/"
                    + (str(file.parent.relative_to(dir)) if str(file.parent.relative_to(dir)) != "." else "")
                    + ("/" if (file.parent / ".slash").is_file() else "")
                )
                if relative_dir_path not in response_parent:
                    response_parent[relative_dir_path] = {}
                json_data = get_json_value_from_file(file)
                response_parent[relative_dir_path][file.stem] = json_data

    def process_dir(dir, response_parent):
        response_parent[dir.name] = {}
        process_files(dir, response_parent[dir.name])

    def create_responses_tree():
        root_dir_path = os.path.join(get_here(), 'fixtures')
        method_subdirs = [d for d in Path(root_dir_path).iterdir() if d.is_dir() and d.name == 'GET']
        for method_subdir in method_subdirs:
            process_dir(method_subdir, responses_map)

    def method(method, url, file='response', headers=None, params=None):
        filename = file
        request_path = url

        response = responses_map.get(method, {}).get(request_path, {}).get(filename)
        return response

    create_responses_tree()
    yield method


@pytest.fixture
def mock_http_call(mock_responses):
    def call(method, url, file='response', headers=None, params=None):

        response = mock_responses(method, url, file=file, headers=headers, params=params)
        if response is not None:
            return response
        http_response = requests.models.Response()
        http_response.status_code = 404
        http_response.reason = "Not Found"
        http_response.url = url
        raise requests.exceptions.HTTPError(response=http_response)

    yield call


@pytest.fixture
def mock_http_get(request, monkeypatch, mock_http_call):
    param = request.param if hasattr(request, 'param') and request.param is not None else {}
    http_error = param.pop('http_error', {})

    def get(url, *args, **kwargs):
        method = 'GET'
        url = get_url_path(url)
        request_path = url.replace('?', '/')
        params = kwargs.get('params')

        if params:
            param_list = []
            for param_name, param_value in params.items():
                if type(param_value) == list:
                    for param_item in param_value:
                        param_list.append((param_name, param_item))
                else:
                    param_list.append((param_name, param_value))

            param_string = '/'.join(f'{param[0]}={str(param[1])}' for param in param_list)
            request_path = f'{url}/{param_string}'

        request_path = request_path.replace(" ", "")
        if http_error and request_path in http_error:
            return http_error[request_path]

        mock_status_code = mock.MagicMock(return_value=200)
        headers = kwargs.get('headers')

        mock_json = mock.MagicMock(return_value=mock_http_call(method, request_path, headers=headers))
        return mock.MagicMock(json=mock_json, status_code=mock_status_code)

    mock_get = mock.MagicMock(side_effect=get)
    monkeypatch.setattr('requests.get', mock_get)
    return mock_get