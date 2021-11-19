# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import os

import mock
import pytest


# @pytest.fixture()
# def mock_argo_cd():
#     f_name = os.path.join(os.path.dirname(__file__), 'fixtures', 'metrics.txt')
#     with open(f_name, 'r') as f:
#         text_data = f.read()
#     with mock.patch(
#         'requests.get',
#         return_value=mock.MagicMock(
#             status_code=200, iter_lines=lambda **kwargs: text_data.split("\n"), headers={'Content-Type': "text/plain"}
#         ),
#     ):
#         yield


@pytest.fixture
def mock_argo_cd():
    f_name = os.path.join(os.path.dirname(__file__), 'fixtures', 'metrics.txt')
    with open(f_name, 'r') as f:
        text_data = f.read()

    with mock.patch(
        'requests.get',
        return_value=mock.MagicMock(
            status_code=200, iter_lines=lambda **kwargs: text_data.split('\n'), headers={'Content-Type': 'text/plain'}
        ),
    ):
        yield


@pytest.fixture
def instance():
    return {'openmetrics_endpoint': 'http://localhost:50000/metrics'}