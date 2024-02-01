from typing import Any, Literal, List, Optional, Union

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
        self.next: Optional['PathNode'] = None
        self.children: List['PathNode'] = None


class NodePath:
    """
    A linked list of PathNodes from schema.

    Args:
        schema (dict): The dictionary schema used to validate the API response.
    """
    def __init__(self, schema: dict = {}):
        self.been_list = False
        if schema:
            self.head = self._construct_linked_list(schema=schema, head=None)
        else:
            self.head = None

    @classmethod
    def from_child_node(cls, node: PathNode) -> 'NodePath':
        """"""
        node_path = cls()
        node_path.head = node
        return node_path

    def _append_children(
        self, 
        children: List[PathNode], 
        head: Optional[PathNode]
    ) -> PathNode:
        """Append children to linked list."""
        node_last = head
        while node_last.next:
            node_last = node_last.next

        node_last.children = children
        return head

    def _append_node_to_bottom(
        self, 
        node: PathNode, 
        head: Optional[PathNode]
    ) -> PathNode:
        """
        Add a node to bottom of the linked list.

        Args:
            node (PathNode): The node to add to list.
        """
        if head is None:
            head = node
            return head

        node_last = head
        while node_last.next:
            node_last = node_last.next

        node_last.next = node
        return head

    def _construct_linked_list(
        self, 
        schema: dict, 
        head: Optional[PathNode]
    ) -> PathNode:
        """
        Construct the linked list.

        Args:
            schema (dict): The dictionary schema used to validate the API response.
        """
        if isinstance(schema, dict):
            if len(schema) != 1:
                raise Exception('dictionary should only have one key')
            key = next(iter(schema))
            schema = schema[key]

            if 'type' not in schema:
                raise ValueError("key 'type' needs to be in schema")
            head = self._append_node_to_bottom(
                node=PathNode(key=key, value_type=schema['type']),
                head=head
            )

            if 'children' in schema:
                schema_children = schema['children']
                if isinstance(schema_children, list):
                    children = [
                        self._construct_linked_list(schema=child, head=None)
                        for child in schema_children
                    ]
                    head = self._append_children(
                        children=children,
                        head=head
                    )
                else:
                    head = self._construct_linked_list(
                        schema=schema_children, 
                        head=head
                    )

        return head
    
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
                "Argument 'type_value' specified for node is invalid"
            )
        
        if expected_type == list:
            self.been_list = True
        return all(isinstance(var, expected_type) for var in obj)