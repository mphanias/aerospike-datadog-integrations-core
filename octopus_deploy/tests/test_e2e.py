# (C) Datadog, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import pytest

from .constants import ALL_METRICS


@pytest.mark.e2e
def test_e2e(dd_agent_check, instance):
    aggregator = dd_agent_check(instance)

    aggregator.assert_metric('octopus_deploy.api.can_connect', 1, tags=['space_name:Default'])
    for metric in ALL_METRICS:
        aggregator.assert_metric(metric)