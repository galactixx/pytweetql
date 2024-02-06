from typing import List

from pytweetql.validation.validation import DirectPathValidation
from pytweetql._utils._data_structures import ListInfo
from pytweetql.validation._base_validation import error_check_output
from pytweetql._typing import Schema

class TwitterList:
    """
    Parsing for an individual Twitter list.
    
    Args:
        name (str): The list name.
        description (str): The list description.
        list_id (str): The list ID.
        mode (str): The mode of the list (public or private).
        member_count (int): The number of members in the list.        
        is_following (bool): Boolean indicating whether the user is following the list.
    """
    def __init__(
        self,
        name: str,
        description: str,
        is_following: bool,
        list_id: str,
        member_count: int,
        mode: str
    ):
        self._name = name
        self._description = description
        self._is_following = is_following
        self._list_id = list_id
        self._member_count = member_count
        self._mode = mode

        self._list = self._parse_list()

    def _parse_list(self) -> ListInfo:
        """
        Parse Twitter list info into structured format.

        Returns:
            ListInfo: The dataclass which holds all relevant Twitter list detail.
        """
        return ListInfo(
            name=self._name,
            description=self._description,
            list_id=self._list_id,
            mode=self._mode,
            member_count=self._member_count,
            is_following=self._is_following
        )
    
    @property
    def twitter_list(self) -> ListInfo:
        """The entire ListInfo dataclass."""
        return self._list
    
    @property
    def name(self) -> str:
        """The list name."""
        return self._list.name
    
    @property
    def description(self) -> str:
        """The list description."""
        return self._list.description
    
    @property
    def list_id(self) -> str:
        """The list ID."""
        return self._list.list_id
    
    @property
    def mode(self) -> str:
        """Whether the list is private or public."""
        return self._list.mode

    @property
    def member_count(self) -> int:
        """The number of members in the list."""
        return self._list.member_count
    
    @property
    def is_following(self) -> bool:
        """Boolean indicating whether the user is following the list."""
        return self._list.is_following


class SingleTwitterList(DirectPathValidation):
    """
    Parsing for a single Twitter list API response.

    Args:
        response (APIResponse): The response from a Twitter API.
        schema (Schema): The schema used to validate the API response.
        endpoint (str): The name the the GraphQL endpoint.
    """
    def __init__(
        self,
        response: List[dict], 
        schema: Schema, 
        endpoint: str
    ):
        super().__init__(response=response)
        self._schema = schema
        self.endpoint = endpoint
        self._twitter_list = self._parse_list()
    
    @property
    def twitter_list(self) -> TwitterList:
        """Returns Twitter list parsed from response."""
        return self._twitter_list

    @error_check_output
    def _parse_list(self) -> TwitterList:
        """
        Parse each individual Twitter list detail from response.

        Returns:
            TwitterList: A TwitterList classe, containing info for the Twitter list detected.
        """
        try:
            return TwitterList(**next(
                self.extract_objects(schema=self._schema)
            ))
        except StopIteration:
            return