from omni_parse.twitter.typing import APIResponse
from omni_parse.twitter.response.user import Users
from omni_parse.twitter.response.tweet import Tweets
from omni_parse.twitter.response.list import Lists
from omni_parse.twitter.validation.graphql_validation import GraphQLValidation

def parse_lists(response: APIResponse) -> Lists:
    """
    Parse each individual list detail from response.

    Returns:
        TwitterList: A class containing the status of the parsing.
    """

    # Validate that it is a list response
    validation = GraphQLValidation(response=response)
    validation.validate_response_list()

    return Lists(
        response=validation.response,
        status=validation.status
    )

def parse_users(response: APIResponse) -> Users:
    """
    Parse each individual user detail from response.

    Returns:
        Users: A class containing the status of the parsing.
    """

    # Validate that it is a user response
    validation = GraphQLValidation(response=response)
    validation.validate_response_user()

    return Users(
        response=validation.response,
        status=validation.status
    )

def parse_tweets(response: APIResponse, remove_promotions: bool = True) -> Tweets:
    """
    Parse each individual tweet detail from response.

    Returns:
        Tweets: A class containing the status of the parsing.
    """

    # Validate that it is a tweet response
    validation = GraphQLValidation(response=response)
    validation.validate_response_tweet()

    return Tweets(
        response=validation.response,
        remove_promotions=remove_promotions,
        status=validation.status
    )