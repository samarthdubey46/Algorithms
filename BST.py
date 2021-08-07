class Node:
    def __init__(self,value=None):
        self.value  = value
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value,self.root)
    def _insert(self,value,root):
        if value < root.value:
            if root.left is None:
                root.left = Node(value)
            else:
                self._insert(value,root.left)
        if value > root.value:
            if root.right is None:
                root.right = Node(value)
            else:
                self._insert(value,root.right)
    def find(self,value):
        if self.root:
            is_found = self._find(value,self.root)
            if is_found:
                return True
            return False
        return None
    def _find(self,value,root):
        if root.value == value:
            return True
        if value > root.value and root.right != None:
            return self._find(value,root.right)
        elif value < root.value and root.left != None:
            return self._find(value,root.left)

bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)
print(bst.find(10))