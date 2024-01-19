from dataclasses import dataclass

@dataclass(frozen=True)
class TweetInfo:
    """
    Dataclass of info pulled from tweet.

    Attributes:
        user_id (str): The user ID of the Twitter account that posted the tweet.
        user_name (str): The user name of the Twitter account that posted the tweet.
        user_screen_name (str): The user screen name of the Twitter account that posted the tweet.
        tweet_id (str): The tweet ID.
        created (str): The UTC date the tweet was created.
        content (str): The text content of the tweet.
        language (str): The language of the text content.
        is_quote (bool): Boolean indicating whether it is a quoted tweet.
        is_retweet (bool): Boolean indicating whether it is a retweet.
        quote_count (int): The number of times the tweet has been quoted.
        reply_count (int): The number of replies on the tweet.
        retweet_count (int): The number of times the tweet has been retweeted.
    """
    user_id: str
    user_name: str
    user_screen_name: str
    tweet_id: str
    created: str
    content: str
    language: str
    is_quote: bool
    is_retweet: bool
    quote_count: int
    reply_count: int
    retweet_count: int