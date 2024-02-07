from typing import Any, Generator, List, Tuple
import copy
import logging

from pytweetql._logging import logging_config
from pytweetql.errors import *
from pytweetql.validation._base_validation import BaseValidation
from pytweetql.validation._nodes import NODES_ERROR_API
from pytweetql._typing import (
    APIResponse, 
    Schema
)
from pytweetql._utils._utils import (
    empty_dictionary,
    extract_dicts_from_list
)
from pytweetql.validation._node_path import (
    NodePath,
    PathNode
)

logger = logging.getLogger(__name__)
logging_config(logger=logger)

def _derive_node_path(schema: dict) -> NodePath:
    """
    Create the node path from a sceham dictionary.

    Args:
        schema (dict): The dictionary schema used to validate the API response.

    Returns:
        NodePath: The node path as a linked list.
    """
    return NodePath(schema=schema)


def _load_schema(schema: Schema) -> Tuple[dict, dict]:
    """
    Validate and load schema specification.
    
    Args:
        schema (Schema): The schema used to validate the API response.

    Returns:
        Tuple[dict, dict]: A tuple of the two Schema components.
    """
    if 'entry' not in schema or 'objects' not in schema:
        raise TypeError("Schema must only have 'entry' and 'objects' keys")
    return schema['entry'], schema['objects']


class DirectPathValidation(BaseValidation):
    """
    Functionality to parse and validate a direct path to dictionaries in a JSON.

    Args:
        response (APIResponse): The response from a Twitter API.
        do_errors (bool): Whether to validate the error format (or main format).
    """
    def __init__(self, response: APIResponse, do_errors: bool = False):
        super().__init__(response=response)

        if not do_errors:
            # Detect and extract any API errors in response
            self._extract_api_errors()

            # Validate response and check if result is empty
            self._validate_response()
        if empty_dictionary(source=self.response):
            self._error(error=ERROR_EMPTY)
        
    def _extract_api_errors(self) -> None:
        """Extract all API errors from response."""
        errors = self.extract_objects(schema=NODES_ERROR_API)
        for error in errors:
            self._error(
                error=generate_api_error(**error)
            )

    def extract_objects(self, schema: Schema) -> Generator[Any, None, None]:
        """
        Extract all relevant objects from the response dictionary.

        Args:
            schema (Schema): The schema used to validate the API response.

        Returns:
            Generator[Any, None, None]: Generator that yields any data type.
        """
        # Load in schema
        schema_entry, schema_objects = _load_schema(schema=schema)

        # Derive entry node path
        node_path_entry = _derive_node_path(schema=schema_entry)

        # Validate schema
        entries = self._validate_schema(
            node_path=node_path_entry,
            response=self.response
        )
        for entry in entries:
            entry_results = {}
            for arg, schema in schema_objects.items():
                results = self._validate_schema(
                    node_path=_derive_node_path(schema=schema),
                    response=[entry]
                )
                for result in results:
                    entry_results.update({arg: result})
            
            if all(arg in entry_results for arg in schema_objects.keys()):
                yield entry_results
            else:
                logger.warning(
                    "Entry found did not have all the expected objects, ignoring..."
                )

    def _validate_schema(
        self,
        node_path: NodePath,
        response: List[dict]
    ) -> Generator[Any, None, None]:
        """
        Validate schema of response by navigating through linked list key path.
        
        Args:
            response (List[dict]): A list of response dictionaries.
            node_path (NodePath): A linked list of PathNodes from schema.

        Returns:
            Generator[Any, None, None]: Generator that yields any data type.
        """
        current_node = node_path.head
        while current_node is not None:

            # Find the current node key in response
            obj = []
            if isinstance(response, list):
                for item in response:
                    if isinstance(item, dict):
                        list_value = item.get(current_node.key)
                        if list_value is not None:
                            obj.append(list_value)

            # Match type of found value to expected type
            if obj and node_path.isinstance_of_type(
                obj=obj, 
                node=current_node
            ):
                response = copy.copy(obj)

                # If we have encountered a list previously,
                # then extract all objects from the result
                if node_path.been_list:
                    response = extract_dicts_from_list(source=response)

                if isinstance(current_node.children, list):
                    for child in current_node.children:
                        records = self._validate_schema(
                            node_path=NodePath.from_child_node(node=child),
                            response=response
                        )
                        for record in records:
                            yield record
                elif not current_node.next:
                    if isinstance(response, list):
                        for record in response:
                            yield record
                    else:
                        yield response
                    break
                else:
                    current_node = current_node.next
            else:
                break