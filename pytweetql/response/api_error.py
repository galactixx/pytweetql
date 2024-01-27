from typing import List

from pytweetql.validation.validation import DirectPathValidation
from pytweetql._utils._data_structures import APIErrorInfo
from pytweetql.validation._base_validation import error_check_output
from pytweetql._typing import Schema

class APIError:
    """"""
    def __init__(self, code: int, message: str):
        self._code = code
        self._message = message

        self._api_error = self._parse_error()

    def _parse_error(self) -> APIErrorInfo:
        """"""
        return APIErrorInfo(code=self._code, message=self._message)

    @property
    def api_error(self) -> APIErrorInfo:
        """"""
        return self._api_error

    @property
    def message(self) -> str:
        """"""
        return self._message

    @property
    def code(self) -> int:
        """"""
        return self._code

class APIErrors(DirectPathValidation):
    """"""
    def __init__(
        self,
        response: List[dict],
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
        Parse each individual error detail from response and load into list.

        Returns:
            List[APIError]: A list of Error classes, one for each API error detected.
        """
        return [
            APIError(**entry) for entry in self.extract_objects(
                schema=self._schema
            )
        ]