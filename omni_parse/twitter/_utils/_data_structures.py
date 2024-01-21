from dataclasses import dataclass

@dataclass(frozen=True)
class Status:
    """
    The status code and description of validation process.
    
    Attributes:
        status_code (int): The status code.
        message (str): Description of the result.
    """
    status_code: int
    message: str

@dataclass(frozen=True)
class UserInfo:
    """
    Dataclass of info pulled from user profile.

    Attributes:
        user_id (str): The user ID of the Twitter account that posted the tweet.
        user_name (str): The user name of the Twitter account that posted the tweet.
        user_screen_name (str): The user screen name of the Twitter account that posted the tweet.
        profile_description (str): The user profile description.
        created (str): The UTC date the user profile was created.
        location (str): The Location of user.
        favourites_count (int): The number of favorites.
        followers_count (int): The number of followers.
        statuses_count (int): The number of statuses.
        is_verified (bool): Boolean indicating whether the user is verified.
    """
    user_id: str
    user_name: str
    user_screen_name: str
    profile_description: str
    created: str
    location: str
    favourites_count: int
    followers_count: int
    statuses_count: int
    is_verified: bool

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
        quote_count (int): The number of times the tweet has been quoted.
        reply_count (int): The number of replies on the tweet.
        retweet_count (int): The number of times the tweet has been retweeted.
        is_quote (bool): Boolean indicating whether it is a quoted tweet.
        is_retweet (bool): Boolean indicating whether it is a retweet.
    """
    user_id: str
    user_name: str
    user_screen_name: str
    tweet_id: str
    created: str
    content: str
    language: str
    quote_count: int
    reply_count: int
    retweet_count: int
    is_quote: bool
    is_retweet: bool