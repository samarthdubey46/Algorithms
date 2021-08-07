class Node:
    def __init__(self,valu):
        self.value = valu
        self.left = None
        self.right = None
class Tree:
    def __init__(self,root):
        self.value = Node(root)
    def print(self,tr):
        if tr == "preorder":
            return self.preoder_print(self.value,"")
        if tr == "inorder":
            return self.inorder(self.value,"")
        if tr == "postorder":
            return self.postorder(self.value,"")
    def preoder_print(self,start,transversal):
        if start:
            transversal += str(start.value) + " -->"
            transversal = self.preoder_print(start.left,transversal)
            transversal = self.preoder_print(start.right,transversal)
        return transversal
    def inorder(self,start,transversal):
        if start:
            transversal = self.inorder(start.left,transversal)
            transversal += str(start.value) + "-->"
            transversal = self.inorder(start.right,transversal)
        return transversal
    def postorder(self,start,transversal):
        if start:
            transversal = self.inorder(start.left, transversal)
            transversal = self.inorder(start.right, transversal)
            transversal += str(start.value) + "-->"
        return transversal
    def height(self,root,i=-1):
        i += 1
        print(i)
        if root.left == None:
            print("Done")
            return i

        else:
            return self.height(root.left,i)
    #      3
#    /   \
#    31   21
#   / \    / \
#   3  4   5  6
tree = Tree(3)
tree.value.right = Node(21)
tree.value.left = Node(31)
tree.value.left.left = Node(3)
tree.value.left.left.left = Node(332)
tree.value.left.right = Node(4)
tree.value.right.left = Node(5)
tree.value.right.right = Node(6)
print(tree.height(tree.value))
print(tree.print("preorder"))
print(tree.print("inorder"))
print(tree.print("postorder"))