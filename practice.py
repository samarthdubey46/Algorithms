class quick_union:
    def __init__(self, n, id=list()):

        self.n = n
        self.id = id

    def union(self, p, q):
        for i in range(self.n + 1):
            self.id.append(i)  # id = [0,1,2,3,4,5,6,7,8,9]
        if p > q:
            self.id[p] = self.id[q]
        elif q > p:
            self.id[q] = self.id[p]
        else:
            self.id[p] = self.id[q]

    def root(self, p):
        print(self.id[p])
        self.id[p] = self.id[self.id[p]]

    def reset(self):
        self.id.clear()
        for i in range(self.n + 1):
            self.id.append(i)
        print(self.id)

    def print(self):
        print(self.id[:self.n + 1])


s = quick_union(9)
s.union(0, 1)
s.union(1,2)
s.union(8,9)
s.union(7,8)
s.union(6,7)
s.union(0,9)
s.root(9)
s.print()
