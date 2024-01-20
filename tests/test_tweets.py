import pytest

from tests.utils import load_json_file
from omni_parse import parsing

parameters = [
    (
    './tests/data/tweet_response.json',
    'success',
    None,
    3
    )
]

@pytest.mark.parametrize('path, status, error, num_tweets', parameters)
def test_tweets(path, status, error, num_tweets) -> None:
    """Test tweet responses."""
    response = load_json_file(path=path)
    tweets = parsing.parse_tweets(response=response)
    assert tweets.status == status
    assert tweets.error == error
    assert tweets.num_tweets == num_tweets