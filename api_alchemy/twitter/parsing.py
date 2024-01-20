from api_alchemy.twitter.typing import APIResponse
from api_alchemy.twitter.response.user import Users
from api_alchemy.twitter.response.tweet import Tweets
from api_alchemy.twitter.validation.graphql_validation import GraphQLValidation

def parse_users(response: APIResponse) -> Users:
    """
    Parse each individual user detail from response.

    Returns:
        Users: A class containing the status of the parsing.
    """

    # Validate that it is a user response
    validation = GraphQLValidation(response=response)
    validation.validate_response()
    validation.validate_response_user()

    return Users(
        response=validation.response,
        status=validation.status,
        error=validation.error
    )

def parse_tweets(response: APIResponse, remove_promotions: bool = True) -> Tweets:
    """
    Parse each individual tweet detail from response.

    Returns:
        Tweets: A class containing the status of the parsing.
    """

    # Validate that it is a tweet response
    validation = GraphQLValidation(response=response)
    validation.validate_response()
    validation.validate_response_tweet()

    return Tweets(
        response=validation.response,
        status=validation.status,
        remove_promotions=remove_promotions,
        error=validation.error
    )