from typing import Any, List, Optional
from datetime import datetime
import logging

from omni_parse._logging import logging_config
from omni_parse.twitter.typing import ResponseKey

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

def return_value(source: ResponseKey, key: str) -> Any:
    """
    Should be used if you are pulling a value at the endpoint of parsing.

    Args:
        source (ResponseKey): A list or dictionary.
        key (str): The key to search for.

    Returns:
        Any: Item pulled from object. 
    """
    found_key = search_key(source=source, key=key)
    if found_key:
        return found_key[0]

def extract_dicts_from_list(source: list) -> List[dict]:
    """
    Recursive function to extract the top-level dictionaries into one list
    from nested lists.

    Args:
        source (list): A list of dictionaries.

    Returns:
        List[dict]: A list with the found dictionary or an empty list.
    """
    def helper(source: list, target: list) -> list:
        if isinstance(source, dict):
            target.append(source)
            
        if isinstance(source, list):
            for item in source:
                target.extend(helper(item, []))
        return target
    
    return helper(source=source, target=[])

def empty_dictionary(source: ResponseKey) -> bool:
    """
    A recursive function to determine if dictionary is empty.

    Args:
        source (ResponseKey): A list or dictionary.

    Returns:
        bool: Whether the object is empty.
    """
    if isinstance(source, dict):
        return all(empty_dictionary(value) for _, value in source.items())
    elif isinstance(source, list):
        return all(empty_dictionary(element) for element in source)
    else:
        return not source

def search_key(source: ResponseKey, key: str) -> List[dict]:
    """
    A recursive function to find all values of a given key within a
    nested dict or list of dicts.

    Args:
        source (ResponseKey): A list or dictionary.
        key (str): The key to search for.

    Returns:
        List[dict]: A list with the found dictionary or an empty list.
    """
    def helper(source: ResponseKey, key: str, target: list) -> list:
        if not source:
            return target

        if isinstance(source, list):
            for e in source:
                target.extend(helper(e, key, []))
            return target

        if isinstance(source, dict) and source.get(key):
            value = source[key]
            if isinstance(value, list):
                target.extend(value)
            else:
                target.append(value)

        if isinstance(source, dict) and source:
            for k in source:
                target.extend(helper(source[k], key, []))
        return target

    return helper(source, key, [])