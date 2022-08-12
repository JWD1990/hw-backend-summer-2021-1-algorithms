from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        def dfs_walk(root: Node, node_list: list[Node]):
            if root in node_list:
                return

            node_list.append(root)

            if not len(root.outbound):
                return

            for node in root.outbound:
                dfs_walk(node, node_list)

        node_lst: list[Node] = []
        dfs_walk(self._root, node_lst)
        return node_lst

    def bfs(self) -> list[Node]:
        def bfs_walk(root: Node, node_list: list[Node]):
            if not len(root.outbound):
                return

            next_nodes: list[Node] = []

            for node in root.outbound:
                if node not in node_list:
                    node_list.append(node)
                    next_nodes.append(node)

            for node in next_nodes:
                bfs_walk(node, node_list)

        node_lst: list[Node] = [self._root]
        bfs_walk(self._root, node_lst)
        return node_lst
