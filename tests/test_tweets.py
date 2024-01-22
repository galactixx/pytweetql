import pytest

from tests.utils import load_json_file
from omni_parse import parsing

parameters = [
    (
    './tests/data/tweet_response.json',
    200,
    'Success',
    3
    ),
    (
    './tests/data/tweet_create_response.json',
    200,
    'Success',
    1
    )
]

@pytest.mark.parametrize('path, status_code, status_message, num_tweets', parameters)
def test_tweets(path, status_code, status_message, num_tweets) -> None:
    """Test tweet responses."""
    response = load_json_file(path=path)
    tweets = parsing.parse_tweets(response=response)
    assert tweets.status_code == status_code
    assert tweets.status_message == status_message
    assert tweets.num_tweets == num_tweets