import pytest

from tests.utils import load_json_file
from pytweetql import parsing

parameters_user_tweets = [
    (
    './tests/data/tweet_response.json',
    200,
    4
    )
]

parameters_tweet_result_by_id = [
    (
    './tests/data/tweet_result_by_id.json',
    200,
    1
    )
]


@pytest.mark.parametrize(
    'path, status_code, num_tweets',
    parameters_user_tweets
)
def test_user_tweets(path, status_code, num_tweets) -> None:
    """Test UserTweets responses."""
    response = load_json_file(path=path)
    tweets = parsing.parse_user_tweets(response=response)
    assert tweets.status_code == status_code
    assert tweets.num_tweets == num_tweets


@pytest.mark.parametrize(
    'path, status_code, num_tweets',
    parameters_tweet_result_by_id
)
def test_tweet_result_by_id(path, status_code, num_tweets) -> None:
    """Test TweetResultByRestId response."""
    response = load_json_file(path=path)
    tweets = parsing.parse_tweet_result_by_id(response=response)
    assert tweets.status_code == status_code
    assert tweets.num_tweets == num_tweets