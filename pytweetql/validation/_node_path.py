from typing import Any, Literal, Optional

_TYPE_MAPPING = {
    'list': list,
    'dict': dict,
    'int': int,
    'str': str,
    'bool': bool
}

class PathNode:
    """
    An individual node in the path.
    """
    def __init__(
        self, 
        key: Any,
        value_type: Literal['str', 'bool', 'list', 'int', 'dict']
    ):
        self.key = key
        self.value_type = value_type
        self.prev: Optional['PathNode'] = None
        self.next: Optional['PathNode'] = None


class NodePath:
    """
    A linked list of PathNodes from schema.

    Args:
        schema (dict): The dictionary schema used to validate the API response.
    """
    def __init__(self, schema: dict):
        self.head = None
        self.been_list = False
        
        self._construct_linked_list(schema=schema)

    def _append_node_to_bottom(self, node: PathNode) -> None:
        """
        Add a node to bottom of the linked list.

        Args:
            node (PathNode): The node to add to list.
        """
        if self.head is None:
            self.head = node
            return

        node_last = self.head
        while node_last.next:
            node_last = node_last.next

        node.prev = node_last
        node_last.next = node

    def _construct_linked_list(self, schema: dict) -> None:
        """
        Construct the doubly linked list.

        Args:
            schema (dict): The dictionary schema used to validate the API response.
        """
        for key, value in schema.items():
            if 'type' not in value:
                raise ValueError('key type needs to be in schema')

            node = PathNode(key=key, value_type=value['type'])
            self._append_node_to_bottom(node=node)
            schema = schema[key]
            
        if 'children' in schema:
            self._construct_linked_list(schema['children'])
    
    def isinstance_of_type(self, obj: Any, node: PathNode) -> bool:
        """
        Validate type of found object in response.

        Args:
            obj (Any): The object found in the step search.
            node (PathNode): A node in the validation schema.

        Returns:
            bool: Whether the object matches the expected type.
        """
        expected_type = _TYPE_MAPPING.get(node.value_type)
        if expected_type is None:
            raise ValueError(
                'Argument type_value specified for node is invalid'
            )

        if self.been_list:
            return all(isinstance(var, expected_type) for var in obj)
        else:
            if expected_type == list:
                self.been_list = True
            return isinstance(obj, expected_type)