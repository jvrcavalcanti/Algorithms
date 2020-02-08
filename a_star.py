from priority_queue import PriorityQueue
from node import Node


def a_star(initial, goal_test, successors, heuristic):
    frontier = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))
    explored = {initial: 0.0}

    while not frontier.empty:
        node = frontier.pop()

        if goal_test(node.state):
            return node

        for parent in successors(node.state):
            new_g = node.g + 1

            if parent in explored:
                continue

            explored.add(parent)
            frontier.push(Node(parent, node, new_g, heuristic(parent)))

    return None
