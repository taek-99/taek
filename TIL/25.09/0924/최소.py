
class DisjointSet:
    def __init__(self, v):
        self.p = [0] * (len(v) + 1)
        self.rank = [0] * (len(v) + 1)


    def make_set(self, x):
        self.p[x] = x
        self.rank[x] = 0

    def find_set(self, x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)

        if px != py:
            if self.rank[px] < self.rank[py]:
                self.p[px] = py
            elif self.rank[px] > self.rank[py]:
                self.p[py] = px
            else:
                self.p[py] = px
                self.rank[px] += 1

disjoint_set = DisjointSet([1, 2, 3, 4, 5, 6])


for i in range(1, len(disjoint_set)):
    disjoint_set.make_set(i)

edged = [(1, 2), (1, 2), (1, 2), (1, 2), (1, 2), ]    