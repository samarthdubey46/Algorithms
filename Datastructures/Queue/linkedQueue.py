from abc import ABC

from Queue import queue
from LinkedList.single import SingleLinkedList
from LinkedList.Node import Node


class Queue(queue.Queue, ABC):
    def __init__(self):
        self.list = SingleLinkedList()
        self.iterList = iter(self.list)

    def __len__(self):
        return self.list.size

    def size(self):
        return self.list.size

    def enqueue(self, elem):
        self.list.addLast(Node(elem))

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is Empty")
        data = self.list.head.data
        self.list.removeFirst()
        return data

    def isEmpty(self):
        return self.size() == 0

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is Empty")
        return self.list.head.data

    def __repr__(self):
        return f"[{''.join([str(i) + ', ' for i in self.list])}]"

    def __iter__(self):
        """
         Called when iteration is initialized
         Return an iterator to allow the user to traverse
         through the elements found inside the queue
        """
        self.iterList = iter(self.list)
        return self

    def __next__(self):
        """
        To move to next element.
        """
        return next(self.iterList)


if __name__ == '__main__':
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q)
    print(q.dequeue())  # 1
    print(q)
    print(q)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  # 5
    print(q.dequeue())  # 1
    print(q.dequeue())  # 2
    print(q.dequeue())  # 3
