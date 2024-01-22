from typing import List

from omni_parse.twitter.response._base_list import BaseList
from omni_parse.twitter.validation._base_validation import BaseStatus
from omni_parse.twitter._utils._data_structures import (
    Status,
    ListInfo
)

class TwitterList(BaseList):
    """
    Parsing for an individual list.
    
    Args:
        result (dict): The raw data section in each list response.
    """
    def __init__(self, entry: dict):
        super().__init__(entry=entry)

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
            is_private=self._is_private,
            is_following=self._is_following
        )
    
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

class Lists(BaseStatus):
    """
    Parsing for a list-related API response.

    Args:
        response (APIResponse): The response from a Twitter API.
        status (Status): The status of the parsing.
    """
    def __init__(
        self,
        response: List[dict],
        status: Status
    ):
        super().__init__(status=status)
        self._response = response

        if self.status_code == 200:
            self._lists = self._parse_lists()
        else:
            self._lists = []
    
    @property
    def lists(self) -> List[TwitterList]:
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
        parsed_lists = []

        for entry in self._response:
            if isinstance(entry, dict):
                parsed_lists.append(
                    TwitterList(entry=entry)
                )

        return parsed_lists