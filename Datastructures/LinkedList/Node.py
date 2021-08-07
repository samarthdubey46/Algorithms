class Node:
    def __init__(self, data: int, next=None,double = False) -> None:
        self.data = data
        self.next = next
        if double:
            self.prev = None

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return str(self.data)
