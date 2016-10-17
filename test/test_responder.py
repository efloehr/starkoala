#
# test/test_responder.py
#


import pytest
import growler
import starkoala
from io import StringIO
from unittest.mock import MagicMock


@pytest.fixture
def mock_protocol():
    m = MagicMock()
    return m


@pytest.fixture
def responder(mock_protocol):
    r = starkoala.TelnetResponder(mock_protocol)
    return r


def test_responder_fixture(responder, mock_protocol):
    assert isinstance(responder, starkoala.TelnetResponder)
    assert responder._handler is mock_protocol


def test_stores_data(responder):
    responder.on_data('hello')
    responder.on_data('friend')
    assert responder._storage == ['hello', 'friend']
