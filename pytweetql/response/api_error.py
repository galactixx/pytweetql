from typing import List

from pytweetql.validation.validation import DirectPathValidation
from pytweetql._utils._data_structures import APIErrorInfo
from pytweetql.validation._base_validation import error_check_output
from pytweetql._typing import (
    APIResponse,
    Schema
)

class APIError:
    """
    Parsing for an individual API error.

    Args:
        code (int): An integer code associated with the error.
        message (str): The message which describes the error.
    """
    def __init__(self, code: int, message: str):
        self._code = code
        self._message = message

        self._api_error = self._parse_error()

    def _parse_error(self) -> APIErrorInfo:
        """
        Parse API error into structured format.
    
        Returns:
            APIErrorInfo: The dataclass which holds all relevant error detail.
        """
        return APIErrorInfo(code=self._code, message=self._message)

    @property
    def api_error(self) -> APIErrorInfo:
        """The entire APIErrorInfo dataclass."""
        return self._api_error

    @property
    def message(self) -> str:
        """The message which describes the error."""
        return self._message

    @property
    def code(self) -> int:
        """An integer code associated with the error."""
        return self._code

class APIErrors(DirectPathValidation):
    """
    Parsing for an error API response.

    Args:
        response (APIResponse): The response from a Twitter API.
        schema (Schema): The schema used to validate the API response.
    """
    def __init__(
        self,
        response: APIResponse,
        schema: Schema
    ):
        super().__init__(response=response, do_errors=True)
        self._schema = schema

        self._api_errors = self._parse_api_errors()

    @property
    def api_errors(self) -> List[APIError]:
        """Returns all the parsed API errors."""
        return self._api_errors

    @property
    def num_api_errors(self) -> int:
        """The number of API errors parsed in response."""
        return len(self._api_errors)
    
    @error_check_output
    def _parse_api_errors(self) -> List[APIError]:
        """
        Parse each individual error detail from response.

        Returns:
            List[APIError]: A list of Error classes, one for each API error detected.
        """
        return [
            APIError(**entry) for entry in self.extract_objects(
                schema=self._schema
            )
        ]