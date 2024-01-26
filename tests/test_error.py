import pytest

from tests.utils import load_json_file
from pytweetql import (
    Error, 
    parsing
)

parameters = [
    (
    './tests/data/error_response.json',
    400,
    [Error(
        code='ERR_007', 
        message='Could not authenticate you', 
        api_code=32
    ),
    Error(
        code='ERR_002', 
        message='Unknown format', 
        api_code=None
    )]
    )
]

@pytest.mark.parametrize('path, status_code, errors', parameters)
def test_error_simple(path, status_code, errors) -> None:
    """Test error responses."""
    response = load_json_file(path=path)
    tweets = parsing.parse_user_tweets(response=response)
    assert tweets.status_code == status_code
    assert tweets.errors == errors