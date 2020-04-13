from data_structure.node import Node
from data_structure.stack import Stack


def dfs(initial, goal_test, successors):
    frontier = Stack()
    frontier.push(Node(initial))
    explored = {initial}

    while not frontier.empty:
        node = frontier.pop()

        if goal_test(node.state):
            return node

        for parent in successors(node.state):
            if parent in explored:
                continue

            explored.add(node.state)
            frontier.push(Node(parent, node))

    return None