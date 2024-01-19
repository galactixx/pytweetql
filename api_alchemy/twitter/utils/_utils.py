from typing import Any, List, Optional
from datetime import datetime
import logging

from api_alchemy._logging import logging_config
from api_alchemy.twitter.typing import ResponseKey

logger = logging.getLogger(__name__)
logging_config(logger=logger)

def verify_boolean(boolean: Any) -> Optional[bool]:
    """
    Verify expected boolean value type. If not a boolean will return None.

    Args:
        boolean (Any): Expected boolean value.

    Returns:
        bool, optional: The boolean value.
    """
    if isinstance(boolean, bool):
        return boolean
    elif isinstance(boolean, str):
        if boolean.lower() == 'true':
            return True
        elif boolean.lower() == 'false':
            return False

def verify_integer(integer: Any) -> int:
    """
    Verify expected integer value type. If not an integer will return None.

    Args:
        integer (Any): Expected integer value.

    Returns:
        int, optional: The integer value.
    """
    if integer is None:
        return
    elif isinstance(integer, int):
        return integer
    elif isinstance(integer, float):
        number_int = int(integer)
        if number_int == integer:
            return number_int
    elif isinstance(integer, str):
        try:
            return int(integer)
        except ValueError:
            return

def verify_datetime(created: Any) -> Optional[str]:
    """
    Verfiy format of created date provided in response.

    Args:
        created (Any): The string representation of the created date field.

    Returns:
        str, optional: The converted UTC string datetime into an ISO format datetime.
    """
    try:
        return datetime.strptime(created, "%a %b %d %H:%M:%S %z %Y").isoformat()
    except ValueError:
        logger.warning(
            f'Incorrect date format specified: {created}, date formatting being skipped'
        )
        return created

def return_value(obj: ResponseKey, key: str) -> Any:
    """
    Should be used if expecting a singular non-(list, tuple, dict) value.

    Args:
        obj (ResponseKey): A list or dictionary.

    Returns:
        Any: Item pulled from dictionary. 
    """
    found_key = find_key(obj=obj, key=key)
    if found_key:
        return found_key[0]

def empty_dictionary(obj: ResponseKey) -> bool:
    """
    A recursive function to determine if dictionary is empty.

    Args:
        obj (ResponseKey): A list or dictionary.

    Returns:
        bool: Whether the dictionary is empty.
    """
    if isinstance(obj, dict):
        return all(empty_dictionary(value) for _, value in obj.items())
    elif isinstance(obj, list):
        return all(empty_dictionary(element) for element in obj)
    else:
        return not obj

def find_key(obj: ResponseKey, key: str) -> List[dict]:
    """
    A recursive function to find all values of a given key within a
    nested dict or list of dicts.

    Args:
        obj (ResponseKey): A list or dictionary.

    Returns:
        List[dict]: A list with the found dictionary or an empty list.
    """
    def helper(obj: ResponseKey, key: str, lst: list) -> list:
        if not obj:
            return lst

        if isinstance(obj, list):
            for e in obj:
                lst.extend(helper(e, key, []))
            return lst

        if isinstance(obj, dict) and obj.get(key):
            lst.append(obj[key])

        if isinstance(obj, dict) and obj:
            for k in obj:
                lst.extend(helper(obj[k], key, []))
        return lst

    return helper(obj, key, [])