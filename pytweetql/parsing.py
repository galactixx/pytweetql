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
        schema=nodes_error_api
    )


def parse_create_list(response: APIResponse) -> TwitterLists:
    """
    Parse Twitter list data from the CreateList endpoint.
    """
    return TwitterLists(
        response=response,
        schema=nodes_list_create,
        endpoint='CreateList'
    )


def parse_following(response: APIResponse) -> Users:
    """
    Parse user data from the Following endpoint.
    """
    return Users(
        response=response,
        schema=nodes_following,
        endpoint='Following'
    )


def parse_list_remove_member(response: APIResponse) -> Users:
    """
    Parse user data from the ListRemoveMember endpoint.
    """
    return Users(
        response=response,
        schema=nodes_list_remove_member,
        endpoint='ListRemoveMember'
    )


def parse_list_add_member(response: APIResponse) -> Users:
    """
    Parse user data from the ListAddMember endpoint.
    """
    return Users(
        response=response,
        schema=nodes_list_add_member,
        endpoint='ListAddMember'
    )


def parse_user_by_id(response: APIResponse) -> Users:
    """
    Parse user data from the UserByRestId endpoint.
    """
    return Users(
        response=response,
        schema=nodes_user_by_rest_id,
        endpoint='UserByRestId'
    )


def parse_users_by_ids(response: APIResponse) -> Users:
    """
    Parse user data from the UsersByRestIds endpoint.
    """
    return Users(
        response=response,
        schema=nodes_users_by_rest_ids,
        endpoint='UsersByRestIds'
    )


def parse_list_members(response: APIResponse) -> Users:
    """
    Parse user data from the ListMembers endpoint.
    """
    return Users(
        response=response,
        schema=nodes_list_members,
        endpoint='ListMembers'
    )


def parse_users_by_screen_name(response: APIResponse) -> Users:
    """
    Parse user data from the UserByScreenName endpoint.
    """
    return Users(
        response=response,
        schema=nodes_user_by_screen_name,
        endpoint='UserByScreenName'
    )


def parse_tweet_result_by_id(
    response: APIResponse, 
    remove_promotions: bool = True
) -> Tweets:
    """
    Parse tweet data from the TweetResultByRestId endpoint.
    """
    return Tweets(
        response=response,
        schema=nodes_tweet_result_by_id,
        remove_promotions=remove_promotions,
        endpoint='TweetResultByRestId'
    )


def parse_user_tweets(
    response: APIResponse, 
    remove_promotions: bool = True
) -> Tweets:
    """
    Parse tweet data from the UserTweets endpoint.
    """
    return Tweets(
        response=response,
        schema=nodes_user_tweets,
        remove_promotions=remove_promotions,
        endpoint='UserTweets'
    )


def parse_create_tweet(
    response: APIResponse, 
    remove_promotions: bool = True
) -> Tweets:
    """
    Parse tweet data from the CreateTweet endpoint.
    """
    return Tweets(
        response=response,
        schema=nodes_create_tweet,
        remove_promotions=remove_promotions,
        endpoint='CreateTweet'
    )


def parse_list_latest_tweets(
    response: APIResponse, 
    remove_promotions: bool = True
) -> Tweets:
    """
    Parse tweet data from the ListLatestTweetsTimeline endpoint.
    """
    return Tweets(
        response=response,
        schema=nodes_list_latest_tweets,
        remove_promotions=remove_promotions,
        endpoint='ListLatestTweetsTimeline'
    )