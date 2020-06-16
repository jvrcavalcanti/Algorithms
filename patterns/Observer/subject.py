from typing import List
from patterns.Observer.observer import Observer

class Subject(object):
    def __init__(self, state):
        self.__state = state
        self.obeservers: List[Observer] = []

    def subscribe(self, observer: Observer):
        self.obeservers.append(observer)

    def unsubscribe(self, observer: Observer):
        self.obeservers.remove(observer)

    def emit(self):
        for observer in self.obeservers:
            observer.handle(self.__state)
    