from api_alchemy.twitter.typing import APIResponse
from api_alchemy.twitter.errors import APIResponseParseError
from api_alchemy.twitter.utils._utils import (
    empty_dictionary,
    find_key
)

def validate_response_tweet(response: APIResponse) -> None:
    """
    Validate the response is concerning tweets.

    Args:
        response (APIResponse): The response from a Twitter API.
    """
    tweet_results_object = find_key(obj=response, key='tweet_results')
    if not tweet_results_object:
        raise APIResponseParseError(
            'This is not a tweet response, please select another parser.'
        )
    
    if empty_dictionary(obj=tweet_results_object):
        raise APIResponseParseError('An accepted response but fields are empty.')

def validate_response(response: APIResponse) -> APIResponse:
    """
    Validate the response from an API referencing several accepted formats.

    Args:
        response (APIResponse): The response from a Twitter API.

    Returns:
        Tweet: A dataclass consolidating all info from tweet.
    """
    validator = ResponseValidation(response=response)
    if validator.validate_graphql_response():
        return validator.response_return
    else:
        raise APIResponseParseError('The response is not recognizable.')

class ResponseValidation:
    """
    Functionality to run initial validation on response.

    Args:
        response (APIResponse): The response from a Twitter API.
    """
    def __init__(self, response: APIResponse):
        self._response = response
        self.response_return: APIResponse = None

    def validate_graphql_response(self) -> bool:
        """
        Validate the response if from GraphQL.

        Args:
            response (dict): The response from the API.

        Returns:
            bool: A boolean indicating whether the response is from GraphQL.
        """
        data_object = find_key(obj=self._response, key='data')
        if data_object:
            self.response_return = data_object
            return True

    def validate_standard_v1_response(self) -> bool:
        """
        """
        pass

    def validate_twitter_v2_response(self) -> bool:
        """
        """
        pass