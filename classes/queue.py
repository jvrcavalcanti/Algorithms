from collections import deque


class Queue(object):
    def __init__(self):
        self._container = deque()

    @property
    def empty(self):
        return not self._container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.popleft()

