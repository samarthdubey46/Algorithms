from abc import ABC

import stack
from LinkedList.single import SingleLinkedList
from LinkedList.Node import Node


class Stack(stack.Stack, ABC):
    def __init__(self):
        self.list = SingleLinkedList()
        self.iterList = iter(self.list)

    def size(self) -> int:
        return self.list.size

    def isEmpty(self):
        return self.list.size == 0

    def push(self, elem):
        self.list.addFirst(Node(elem))

    def pop(self):
        if self.isEmpty():
            raise Exception('Empty Stack')
        else:
            self.list.removeFirst()

    def peek(self):
        if self.isEmpty():
            raise Exception('Empty Stack')
        return self.list.head.data

    def __iter__(self):
        """
         Called when iteration is initialized
        """
        self.iterList = iter(self.list)
        return self

    def __next__(self):
        """
        To move to next element.
        """
        return next(self.iterList)

    def __repr__(self):
        return f"[{''.join([str(i) + ', ' for i in self.list])}]"


# stack = Stack()
# stack.push(21)
# stack.push(41)
# stack.push(21)
# stack.push(1121)
# stack.pop()
# print(stack)
