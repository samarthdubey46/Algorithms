from abc import ABC, abstractmethod


class Queue(ABC):

    @abstractmethod
    def enqueue(self, elem):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass
