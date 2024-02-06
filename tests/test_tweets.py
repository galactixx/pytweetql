import pytest

from tests.utils import load_json_file
from pytweetql import (
    parsing, 
    TweetInfo
)

parameters_user_tweets = [
    (
    './tests/data/user_tweets.json',
    200,
    9
    )
]

parameters_tweet_result_by_id = [
    (
    './tests/data/tweet_result_by_id.json',
    200,
    TweetInfo(
        user_id='44196397',
        user_name='Elon Musk',
        user_screen_name='elonmusk',
        tweet_id='1749150144392532007',
        created='2024-01-21T19:21:06+00:00',
        content='An 𝕏 spam/scam bot accidentally flagged many legitimate accounts today. This is being fixed.',
        language='en',
        tweet_url='https://twitter.com/elonmusk/status/1749150144392532007',
        quote_count=2585,
        reply_count=14709,
        retweet_count=18193,
        is_quote=False,
        is_retweet=False
    )
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
    TweetInfo(
        user_id='1744931660808720384',
        user_name='Plutarch Glicia',
        user_screen_name='dandywarlock2',
        tweet_id='1750725790956761270',
        created='2024-01-26T03:42:10+00:00',
        content='Space travel is amazing',
        language='en',
        tweet_url='https://twitter.com/dandywarlock2/status/1750725790956761270',
        quote_count=0,
        reply_count=0,
        retweet_count=0,
        is_quote=False,
        is_retweet=False
    )
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
    'path, status_code, tweet',
    parameters_tweet_result_by_id
)
def test_tweet_result_by_id(path, status_code, tweet) -> None:
    """Test TweetResultByRestId response."""
    response = load_json_file(path=path)
    single_tweet = parsing.parse_tweet_result_by_id(response=response)
    assert single_tweet.status_code == status_code
    assert single_tweet.tweet.tweet == tweet


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
    'path, status_code, tweet',
    parameters_create_tweet
)
def test_create_tweet(path, status_code, tweet) -> None:
    """Test CreateTweet response."""
    response = load_json_file(path=path)
    single_tweet = parsing.parse_create_tweet(response=response)
    assert single_tweet.status_code == status_code
    assert single_tweet.tweet.tweet == tweet