# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from types import MappingProxyType
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, field_validator, model_validator

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, validators


class CollectPerInstanceFilters(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    cluster: Optional[tuple[str, ...]] = None
    datastore: Optional[tuple[str, ...]] = None
    host: Optional[tuple[str, ...]] = None
    vm: Optional[tuple[str, ...]] = None


class IncludeEvent(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    excluded_messages: Optional[tuple[str, ...]] = None


class MetricFilters(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    cluster: Optional[tuple[str, ...]] = None
    datacenter: Optional[tuple[str, ...]] = None
    datastore: Optional[tuple[str, ...]] = None
    host: Optional[tuple[str, ...]] = None
    vm: Optional[tuple[str, ...]] = None


class MetricPatterns(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[str, ...]] = None


class ResourceFilter(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    patterns: Optional[tuple[str, ...]] = None
    property: Optional[str] = None
    resource: Optional[str] = None
    type: Optional[str] = None


class AuthToken(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    reader: Optional[MappingProxyType[str, Any]] = None
    writer: Optional[MappingProxyType[str, Any]] = None


class Proxy(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    http: Optional[str] = None
    https: Optional[str] = None
    no_proxy: Optional[tuple[str, ...]] = None


class RestApiOptions(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    allow_redirects: Optional[bool] = None
    auth_token: Optional[AuthToken] = None
    auth_type: Optional[str] = None
    aws_host: Optional[str] = None
    aws_region: Optional[str] = None
    aws_service: Optional[str] = None
    connect_timeout: Optional[float] = None
    extra_headers: Optional[MappingProxyType[str, Any]] = None
    headers: Optional[MappingProxyType[str, Any]] = None
    kerberos_auth: Optional[str] = None
    kerberos_cache: Optional[str] = None
    kerberos_delegate: Optional[bool] = None
    kerberos_force_initiate: Optional[bool] = None
    kerberos_hostname: Optional[str] = None
    kerberos_keytab: Optional[str] = None
    kerberos_principal: Optional[str] = None
    log_requests: Optional[bool] = None
    ntlm_domain: Optional[str] = None
    password: Optional[str] = None
    persist_connections: Optional[bool] = None
    proxy: Optional[Proxy] = None
    read_timeout: Optional[float] = None
    request_size: Optional[float] = None
    skip_proxy: Optional[bool] = None
    timeout: Optional[float] = None
    tls_ca_cert: Optional[str] = None
    tls_cert: Optional[str] = None
    tls_ciphers: Optional[tuple[str, ...]] = None
    tls_ignore_warning: Optional[bool] = None
    tls_private_key: Optional[str] = None
    tls_protocols_allowed: Optional[tuple[str, ...]] = None
    tls_use_host_header: Optional[bool] = None
    tls_verify: Optional[bool] = None
    use_legacy_auth_encoding: Optional[bool] = None
    username: Optional[str] = None


class InstanceConfig(BaseModel):
    model_config = ConfigDict(
        validate_default=True,
        arbitrary_types_allowed=True,
        frozen=True,
    )
    attributes_prefix: Optional[str] = None
    batch_property_collector_size: Optional[int] = None
    batch_tags_collector_size: Optional[int] = None
    collect_attributes: Optional[bool] = None
    collect_events: Optional[bool] = None
    collect_events_only: Optional[bool] = None
    collect_per_instance_filters: Optional[CollectPerInstanceFilters] = None
    collect_property_metrics: Optional[bool] = None
    collect_tags: Optional[bool] = None
    collect_vsan_data: Optional[bool] = None
    collection_level: Optional[int] = None
    collection_type: Optional[str] = None
    connection_reset_timeout: Optional[int] = None
    disable_generic_tags: Optional[bool] = None
    empty_default_hostname: bool
    event_resource_filters: Optional[tuple[str, ...]] = None
    excluded_host_tags: Optional[tuple[str, ...]] = None
    host: str
    hostname_transform: Optional[str] = None
    include_datastore_cluster_folder_tag: Optional[bool] = None
    include_events: Optional[tuple[IncludeEvent, ...]] = None
    max_historical_metrics: Optional[int] = None
    metric_filters: Optional[MetricFilters] = None
    metric_patterns: Optional[MetricPatterns] = None
    metrics_per_query: Optional[int] = None
    min_collection_interval: Optional[float] = None
    password: str
    refresh_infrastructure_cache_interval: Optional[int] = None
    refresh_metrics_metadata_cache_interval: Optional[int] = None
    resource_filters: Optional[tuple[ResourceFilter, ...]] = None
    rest_api_options: Optional[RestApiOptions] = None
    service: Optional[str] = None
    ssl_cafile: Optional[str] = None
    ssl_capath: Optional[str] = None
    ssl_verify: Optional[bool] = None
    tags: Optional[tuple[str, ...]] = None
    tags_prefix: Optional[str] = None
    threads_count: Optional[int] = None
    tls_ignore_warning: Optional[bool] = None
    use_collect_events_fallback: Optional[bool] = None
    use_guest_hostname: Optional[bool] = None
    use_legacy_check_version: bool
    username: str
    vm_hostname_suffix_tag: Optional[str] = None

    @model_validator(mode='before')
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @field_validator('*', mode='before')
    def _validate(cls, value, info):
        field = cls.model_fields[info.field_name]
        field_name = field.alias or info.field_name
        if field_name in info.context['configured_fields']:
            value = getattr(validators, f'instance_{info.field_name}', identity)(value, field=field)
        else:
            value = getattr(defaults, f'instance_{info.field_name}', lambda: value)()

        return validation.utils.make_immutable(value)

    @model_validator(mode='after')
    def _final_validation(cls, model):
        return validation.core.check_model(getattr(validators, 'check_instance', identity)(model))
