from typing import List

from pytweetql.validation.validation import DirectPathValidation
from pytweetql._utils._data_structures import ListInfo
from pytweetql._typing import Schema

class TwitterList:
    """
    Parsing for an individual Twitter list.
    
    Args:
        entry (dict): The raw data section in each list response.
    """
    def __init__(
        self,
        description: str,
        is_following: bool,
        list_id: str,
        member_count: int,
        mode: str
    ):
        self._description = description
        self._is_following = is_following
        self._list_id = list_id
        self._member_count = member_count
        self._mode = mode

        self._list = self._parse_list()

    def _parse_list(self) -> ListInfo:
        """
        Parse list dictionaries into structured format.

        Returns:
            ListInfo: The dataclass which holds all relevant list detail.
        """
        return ListInfo(
            name=self._name,
            description=self._description,
            list_id=self._list_id,
            member_count=self._member_count,
            mode=self._mode,
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
    def member_count(self) -> int:
        """The number of members in the list."""
        return self._list.member_count

    @property
    def is_private(self) -> bool:
        """Boolean indicating whether the list is private."""
        return self._list.is_private
    
    @property
    def is_following(self) -> bool:
        """Boolean indicating whether the user is following the list."""
        return self._list.is_following


class TwitterLists(DirectPathValidation):
    """
    Parsing for a list-related API response.

    Args:
        response (List[dict]): The response from a Twitter API.
        status (Status): The status of the parsing.
    """
    def __init__(
        self,
        response: List[dict], 
        schema: Schema, 
        endpoint: str
    ):
        super().__init__(response=response, schema=schema)
        self.endpoint = endpoint

        self._lists = self._parse_lists()
    
    @property
    def twitter_lists(self) -> List[TwitterList]:
        """Returns all the parsed lists."""
        return self._lists

    @property
    def num_lists(self) -> int:
        """The number of lists parsed in response."""
        return len(self._lists)

    def _parse_lists(self) -> List[TwitterList]:
        """
        Parse each individual list detail from response and load into list.

        Returns:
            List[TwitterList]: A list of TwitterList classes, one for each list detected.
        """
        return [TwitterList(**entry) for entry in self.validate_and_parse()]