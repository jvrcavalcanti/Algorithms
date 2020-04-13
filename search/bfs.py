from data_structure import Node
from data_structure import Queue


def bfs(initial, goal_test, successors):
    frontier = Queue()
    frontier.push(Node(initial))
    explored = {initial}

    while not frontier.empty:
        node: Node = frontier.pop()

        if goal_test(node.state):
            return node

        for parent in successors(node.state):
            if parent in explored:
                continue

            explored.add(node.state)
            frontier.push(Node(parent, node))
    return None
