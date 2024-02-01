from typing import List

from pytweetql.response.twitterlist import TwitterLists
from pytweetql.validation._nodes import *
from pytweetql._typing import APIResponse
from pytweetql.response.user import Users
from pytweetql.response.tweet import Tweets
from pytweetql.response.api_error import APIErrors

def parse_api_errors(response: APIResponse) -> APIErrors:
    """
    Parse any API errors found in response.
    """
    return APIErrors(
        response=response,
        schema=NODES_ERROR_API
    )


def parse_create_list(response: APIResponse) -> TwitterLists:
    """
    Parse Twitter list data from the CreateList endpoint.
    """
    return TwitterLists(
        response=response,
        schema=NODES_LIST_CREATE,
        endpoint='CreateList'
    )


def parse_following(response: APIResponse) -> Users:
    """
    Parse user data from the Following endpoint.
    """
    return Users(
        response=response,
        schema=NODES_FOLLOWING,
        endpoint='Following'
    )


def parse_list_remove_member(response: APIResponse) -> Users:
    """
    Parse user data from the ListRemoveMember endpoint.
    """
    return Users(
        response=response,
        schema=NODES_LIST_REMOVE_MEMBER,
        endpoint='ListRemoveMember'
    )


def parse_list_add_member(response: APIResponse) -> Users:
    """
    Parse user data from the ListAddMember endpoint.
    """
    return Users(
        response=response,
        schema=NODES_LIST_ADD_MEMBER,
        endpoint='ListAddMember'
    )


def parse_user_by_id(response: APIResponse) -> Users:
    """
    Parse user data from the UserByRestId endpoint.
    """
    return Users(
        response=response,
        schema=NODES_USER_BY_REST_ID,
        endpoint='UserByRestId'
    )


def parse_users_by_ids(response: APIResponse) -> Users:
    """
    Parse user data from the UsersByRestIds endpoint.
    """
    return Users(
        response=response,
        schema=NODES_USERS_BY_REST_IDS,
        endpoint='UsersByRestIds'
    )


def parse_list_members(response: APIResponse) -> Users:
    """
    Parse user data from the ListMembers endpoint.
    """
    return Users(
        response=response,
        schema=NODES_LIST_MEMBERS,
        endpoint='ListMembers'
    )


def parse_users_by_screen_name(response: APIResponse) -> Users:
    """
    Parse user data from the UserByScreenName endpoint.
    """
    return Users(
        response=response,
        schema=NODES_USER_BY_SCREEN_NAME,
        endpoint='UserByScreenName'
    )


def parse_tweet_result_by_id(response: APIResponse, users: List[str] = []) -> Tweets:
    """
    Parse tweet data from the TweetResultByRestId endpoint.
    """
    return Tweets(
        response=response,
        schema=NODES_TWEET_RESULT_BY_ID,
        endpoint='TweetResultByRestId',
        users=users
    )


def parse_user_tweets(response: APIResponse, users: List[str] = []) -> Tweets:
    """
    Parse tweet data from the UserTweets endpoint.
    """
    return Tweets(
        response=response,
        schema=NODES_USER_TWEETS,
        endpoint='UserTweets',
        users=users
    )


def parse_create_tweet(response: APIResponse, users: List[str] = []) -> Tweets:
    """
    Parse tweet data from the CreateTweet endpoint.
    """
    return Tweets(
        response=response,
        schema=NODES_CREATE_TWEET,
        endpoint='CreateTweet',
        users=users
    )


def parse_list_latest_tweets(response: APIResponse, users: List[str] = []) -> Tweets:
    """
    Parse tweet data from the ListLatestTweetsTimeline endpoint.
    """
    return Tweets(
        response=response,
        schema=NODES_LIST_LATEST_TWEETS,
        endpoint='ListLatestTweetsTimeline',
        users=users
    )