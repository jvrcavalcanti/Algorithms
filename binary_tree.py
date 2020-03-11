class Node(object):
    def __init__(self, state):
        self.state = state
        self.left = None
        self.right = None

    def search(self, state):
        if state == self.state:
            return self.state
        
        if state > self.state and self.left is not None:
            return self.left.search(state)

        if state < self.state and self.right is not None:
            return self.right.search(state)

    def add(self, state):
        if state > self.state:
            if self.left is None:
                self.left = Node(state)
                return self.left
            return self.left.add(state)

        if state < self.state:
            if self.right is None:
                self.right = Node(state)
                return self.right
            return self.right.add(state)

    def traversal(self):
        if self.right is not None:
            print(self.right.state)

        print(self.state)

        if self.left is not None:
            print(self.left.state)

    def __repr__(self):
        return "State: " + str(self.state)


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, state):
        if self.root.state == state:
            return state

        if state > self.root.state:
            return self.root.left.search(state)

        if state < self.root.state:
            return self.root.right.search(state)

    def add(self, state):
        if state > self.root.state:
            if self.root.left is None:
                self.root.left = Node(state)
                return self.root.left
            return self.root.left.add(state)

        if state < self.root.state:
            if self.root.right is None:
                self.root.right = Node(state)
                return self.root.right
            return self.root.right.add(state)

    def traversal(self):
        if self.root.right is not None:
            self.root.right.traversal()
        print(self.root.state)
        if self.root.left is not None:
            self.root.left.traversal()


if __name__ == "__main__":
    tree = BinaryTree(9)
    tree.add(7)
    tree.add(8)
    tree.add(10)
    tree.add(6)
    tree.traversal()