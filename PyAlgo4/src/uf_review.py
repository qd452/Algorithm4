__author__ = 'dong.qu'


class UF():
    """
    quick union
    """
    def __init__(self, N):
        self.N = N
        self.parent_val = list(range(N))

    def find_root(self, p_idx):
        while p_idx != self.parent_val[p_idx]:
            p_idx = self.parent_val[p_idx]
        return p_idx

    def union(self, p, q):
        p_rt = self.find_root(p)
        q_rt = self.find_root(q)
        if p_rt == q_rt:
            pass
        else:
            self.parent_val[q] = p_rt
        self.N -= 1

    def connected(self, p, q):
        return self.find_root(p) == self.find_root(q)

    def count(self):
        return self.N

uf = UF(6)
uf.union(3,4)
print(uf.parent_val)
uf.union(4,5)
uf.union(1,3)
uf.union(1,4)
print(uf.parent_val)
print(uf.connected(1,5))
