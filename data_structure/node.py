class Node(object):
    def __init__(self, state, parent=None, g=0.0, h=0.0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h

    def __lt__(self, other):
        return self.g + self.h < other.g + other.h

    def __eq__(self, other):
        return self.g + self.h == other.g + other.h


# def node_to_path(node: Node):
#     path = [node]
#     while node.parent is not None:
#         node = node.parent
#         path.append(node)
#     path.reverse()
#     return path

