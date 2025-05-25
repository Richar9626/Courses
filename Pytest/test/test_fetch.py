from unittest.mock import patch
from fetch_www import parse


@patch("fetch_www.fetch_net")
def test_parse_from_fetch_net(mock_get):
    """meh"""
    mock_get.return_value = "def"
    assert parse() == "abc123"