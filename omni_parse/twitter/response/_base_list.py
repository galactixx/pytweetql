from omni_parse.twitter._utils._utils import (
    verify_boolean,
    verify_integer
)

class BaseList:
    """
    Parsing from the raw response of an individual list.

    Args:
        entry (dict): The raw data section in each list response.
    """
    def __init__(self, entry: dict):
        self._entry = entry

    @property
    def _name(self) -> str:
        """The list name."""
        return self._entry.get('name')
    
    @property
    def _description(self) -> str:
        """The list description."""
        return self._entry.get('description')
    
    @property
    def _list_id(self) -> str:
        """The list ID."""
        return self._entry.get('id_str')
    
    @property
    def _member_count(self) -> int:
        """The number of members in the list."""
        return verify_integer(integer=self._entry.get('member_count'))

    @property
    def _is_private(self) -> bool:
        """Boolean indicating whether the list is private."""
        return verify_boolean(boolean=self._entry.get('member_count'))
    
    @property
    def _is_following(self) -> bool:
        """Boolean indicating whether the user is following the list."""
        return verify_boolean(boolean=self._entry.get('member_count'))