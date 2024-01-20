import pytest

from tests.utils import load_json_file
from omni_parse import (
    parsing,
    ValidationError
)

parameters = [
    (
    './tests/data/error_response.json',
    'failure',
    ValidationError(
        code=105,
        error='API request error: Could not authenticate you'
    )
    )
]

@pytest.mark.parametrize('path, status, error', parameters)
def test_error_simple(path, status, error) -> None:
    """Test error responses."""
    response = load_json_file(path=path)
    tweets = parsing.parse_tweets(response=response)
    assert tweets.status == status
    assert tweets.error == error