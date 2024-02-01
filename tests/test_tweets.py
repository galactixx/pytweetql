import pytest

from tests.utils import load_json_file
from pytweetql import parsing

parameters_user_tweets = [
    (
    './tests/data/user_tweets.json',
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

parameters_list_latest_tweets = [
    (
    './tests/data/list_latest_tweets.json',
    200,
    12
    )
]

parameters_create_tweet = [
    (
    './tests/data/create_tweet.json',
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


@pytest.mark.parametrize(
    'path, status_code, num_tweets',
    parameters_list_latest_tweets
)
def test_list_latest_tweets(path, status_code, num_tweets) -> None:
    """Test ListLatestTweetsTimeline response."""
    response = load_json_file(path=path)
    tweets = parsing.parse_list_latest_tweets(response=response)
    assert tweets.status_code == status_code
    assert tweets.num_tweets == num_tweets


@pytest.mark.parametrize(
    'path, status_code, num_tweets',
    parameters_create_tweet
)
def test_create_tweet(path, status_code, num_tweets) -> None:
    """Test CreateTweet response."""
    response = load_json_file(path=path)
    tweets = parsing.parse_create_tweet(response=response)
    assert tweets.status_code == status_code
    assert tweets.num_tweets == num_tweets