from . import Node


class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
        self.travIter = None

    def __len__(self):
        return self.size

    def clear(self):
        if self.size > 0:
            trav = self.head
            while trav is not None:
                n = trav.next
                trav.prev = trav.next = None
                trav.data = None
                trav = n
            self.head = None
            self.tail = None
            self.size = 0

    def addFirst(self, node: Node):
        node.next = self.head
        self.head = node
        if self.size == 0:
            self.tail = node
        self.size += 1

    def addLast(self, node: Node) -> None:
        if self.size == 0:
            self.addFirst(node)
        else:
            self.tail.next = node
            self.tail = node
            self.size += 1

    def add_at(self, index: int, node: Node):
        if index > self.size + 1 or index < 0:
            raise IndexError()
        if index - 1 == self.size:
            self.addLast(node)
        if index == 0:
            self.addFirst(node)
        else:
            trav = self.head
            for i in range(1, index - 1):
                trav = trav.next
            print(trav)
            temp = trav.next
            trav.next = node
            node.next = temp
            self.size += 1

    def removeFirst(self):
        self.head = self.head.next
        self.size -= 1

    def removeLast(self):
        temp = self.head
        for i in range(1, self.size - 1):
            temp = temp.next
        temp.next = None
        self.tail = temp
        self.size -= 1

    def indexOf(self, obj):
        index = 0
        trav = self.head
        while trav is not None:
            if trav.data == obj:
                return index
            index += 1
            trav = trav.next

        return -1

    def remove_obj(self, obj):
        index = self.indexOf(obj)
        if index == -1:
            raise IndexError()
        if index == 0:
            self.removeFirst()
        else:
            if index == self.size - 1:
                self.removeLast()
            else:
                trav = self.head
                for i in range(1, index):
                    trav = trav.next
                trav.next = trav.next.next
                self.size -= 1

    def __iter__(self):
        """
        Called when iteration is initialized
        """
        self.travIter = self.head
        return self

    def __next__(self):
        """
        To move to next element.
        """
        # Stop iteration if limit is reached
        if self.travIter is None:
            raise StopIteration

        # Store current travIter.data
        data = self.travIter.data
        self.travIter = self.travIter.next

        # Else increment and return old value
        return data

    def reverse(self):
        head = self.head
        curr = self.head
        prev = None
        while True:
            temp_next = curr.next
            self.head.next = prev
            if temp_next == None:
                break
            prev = self.head

            self.head = temp_next
            curr = temp_next
        self.tail = head

    def __repr__(self):
        sb = ""
        trav = self.head
        while trav is not None:
            sb = sb + f"({str(trav.data)})"
            if trav.next is not None:
                sb = sb + ' -> '
            trav = trav.next
        return str(sb)

# LinkedList = SingleLinkedList()
# LinkedList.addfirst(Node(2))
# LinkedList.addfirst(Node(3))
# LinkedList.addLast(Node(6))
# LinkedList.add_at(0, Node(1))
# # LinkedList.removefirst()
# # LinkedList.remove_obj(2)
# print("Normal = ",LinkedList)
# LinkedList.reverse()
# print("Reversed = ",LinkedList)
# print("Size = ", LinkedList.size)
# print("Head = ", LinkedList.head)
# print("Tail = ", LinkedList.tail)
# print("index = ", LinkedList.indexof(1))
