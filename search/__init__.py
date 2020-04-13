from search.a_star import a_star
from search.bfs import bfs
from search.dfs import dfs
from data_structure import Node


def node_path(node: Node):
    # if node is None:
    #     return []

    path = [node.state]

    while node.parent is not None:
        node = node.parent
        path.append(node.state)

    path.reverse()
    return path