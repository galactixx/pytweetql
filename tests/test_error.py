import pytest

from tests.utils import load_json_file
from pytweetql import (
    Error, 
    parsing
)

parameters = [
    (
    './tests/data/error.json',
    400,[
    Error(
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

parameters_api_error = [
    (
    './tests/data/error.json',
    200,
    1
    )
]


@pytest.mark.parametrize(
    'path, status_code, errors', 
    parameters
)
def test_error_simple(path, status_code, errors) -> None:
    """Test API error responses."""
    response = load_json_file(path=path)
    tweets = parsing.parse_user_tweets(response=response)
    assert tweets.status_code == status_code
    assert tweets.errors == errors


@pytest.mark.parametrize(
    'path, status_code, errors', 
    parameters_api_error
)
def test_error_response(path, status_code, errors) -> None:
    """Test API error responses."""
    response = load_json_file(path=path)
    tweets = parsing.parse_api_errors(response=response)
    assert tweets.status_code == status_code
    assert tweets.num_api_errors == errors