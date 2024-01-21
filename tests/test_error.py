import pytest

from tests.utils import load_json_file
from omni_parse import parsing

parameters = [
    (
    './tests/data/error_response.json',
    502,
    'API request error: Could not authenticate you'
    )
]

@pytest.mark.parametrize('path, status_code, status_message', parameters)
def test_error_simple(path, status_code, status_message) -> None:
    """Test error responses."""
    response = load_json_file(path=path)
    tweets = parsing.parse_tweets(response=response)
    assert tweets.status_code == status_code
    assert tweets.status_message == status_message