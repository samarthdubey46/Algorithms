from _collections import deque
class UF:

    def __init__(self):
        self.s = set()
    def union(self,p,q):

        if p and q in self.s:
            pass
        else:
            self.s.add(p)
            self.s.add(q)
        print(self.s)
    def connected(self,a,b):
        print(self.s)
        if len(self.s) == 1:
            print('only one element in set')
        if len(self.s) != 0:
            if a and b  not in self.s:
                print(' not Connected')
            else:
                print('Connected')
        else:
            print('no items in list')

    # def find(self):
    #
    def Know(self):

        if len(self.s) != 0:
            print(self.s)
        else:
            print('No items are connected')

    def Clear(self):

        self.s.clear()

# class is_connected():
#
#     def __init__(self,n,id = deque()):
#         self.id = id
#         self.n = n
#
#     def union(self,p,q):
#
#         for i in range(self.n+1):
#             self.id.append(i)
#         if self.id[p] == self.id[q]:
#             print('connected')
#         else:
#             self.id[p] = self.id.index(q)
#             print('now connected')
c = UF()
c.union(2,5)
c.connected(1,87)
s = {1,2,3,4}
print(max(s))
