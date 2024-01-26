from typing import Any, Literal, Optional

class PathNode:
    """
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
    Turn a list of PathNode dataclasses into an interator.

    Args:
        schema (dict): The linked list dictionary schema.
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
            schema (dict): The linked list dictionary schema.
        """
        for key, value in schema.items():
            if 'type' not in value:
                raise ValueError('key type needs to be in schema')

            node = PathNode(key=key, value_type=value['type'])
            self._append_node_to_bottom(node=node)
            schema = schema[key]
            
        if 'children' in schema:
            self._construct_linked_list(schema['children'])

    def _type_check(self, key_search: Any, type: type) -> bool:
        """
        """
        if self.been_list:
            return all(isinstance(var, type) for var in key_search)
        else:
            if type == list:
                self.been_list = True
            return isinstance(key_search, type)
    
    def isinstance_of_type(self, key_search: Any, node: PathNode) -> bool:
        """"""
        if node.value_type == 'list':
            return self._type_check(key_search=key_search, type=list)
        elif node.value_type == 'dict':
            return self._type_check(key_search=key_search, type=dict)
        elif node.value_type == 'int':
            return self._type_check(key_search=key_search, type=int)
        elif node.value_type == 'str':
            return self._type_check(key_search=key_search, type=str)
        elif node.value_type == 'bool':
            return self._type_check(key_search=key_search, type=bool)
        else:
            raise ValueError(
                'Argument type_value specified for node is invalid'
            )