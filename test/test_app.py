#
# test/test_app.py
#


import pytest
import growler
import starkoala
from unittest.mock import MagicMock


@pytest.fixture
def mock_protocol():
    m = MagicMock()
    return m


@pytest.fixture
def app():
    a = starkoala.Application()
    return a


def test_app_fixture(app):
    assert isinstance(app, starkoala.Application)
