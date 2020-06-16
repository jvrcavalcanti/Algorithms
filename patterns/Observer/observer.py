from abc import ABC, abstractmethod

class Observer():
    @abstractmethod
    def handle(self, state):
        pass