class Heap:
    def __init__(self,a:list):
        self.list = sorted(a,reverse=True)
    def pop(self):
        self.list.remove(self.list[-1])
    def add(self,number):
        self.list.append(number)
        self.list.sort(reverse=True)
    def pop_add(self,a):
        self.pop()
        self.add(a)
    def printklargest(self,k):
        print(self.list[:k])
    def printheap(self):
        print(self.list)
li = [2,5,2,7,4]
heap =Heap(li)
heap.pop()
heap.pop()
heap.add(21)
heap.add(1)
heap.pop_add(4)
heap.printheap()


