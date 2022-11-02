# 281. 天际线问题
import collections
from typing import List


class MaxSegTree:
    def __init__(self):
        self.m = collections.defaultdict(int)
        self.lazy = collections.defaultdict(int)

    def update(self, L, R, C, l, r, rt):
        if l >= L and r <= R:
            self.m[rt] = max(self.m[rt], C)
            self.lazy[rt] = max(self.lazy[rt], C)
            return
        mid = l + ((r - l) >> 1)
        self.pushDown(rt)
        if mid >= L and l <= R:
            self.update(L, R, C, l, mid, rt << 1)
        if r >= L and mid + 1 <= R:
            self.update(L, R, C, mid + 1, r, rt << 1 | 1)
        self.pushUp(rt)

    def query(self, L, R, l, r, rt):
        if l >= L and r <= R:
            return self.m[rt]
        mid = l + ((r - l) >> 1)
        self.pushDown(rt)
        ans = 0
        if mid >= L and l <= R:
            ans = max(ans, self.query(L, R, l, mid, rt << 1))
        if r >= L and mid + 1 <= R:
            ans = max(ans, self.query(L, R, mid + 1, r, rt << 1 | 1))
        self.pushUp(rt)
        return ans

    def pushDown(self, rt):
        if self.lazy[rt]:
            self.lazy[rt << 1] = max(self.lazy[rt << 1], self.lazy[rt])
            self.lazy[rt << 1 | 1] = max(self.lazy[rt << 1 | 1], self.lazy[rt])
            self.m[rt << 1] = max(self.m[rt << 1], self.lazy[rt])
            self.m[rt << 1 | 1] = max(self.m[rt << 1 | 1], self.lazy[rt])
            self.lazy[rt] = 0

    def pushUp(self, rt):
        self.m[rt] = max(self.m[rt << 1], self.m[rt << 1 | 1])


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 区间最大值问题
        # 1. 离散化
        s = set()
        for build in buildings:
            s.add(build[0])
            s.add(build[1])
        l = list(s)
        l.sort()
        s = {i: ind + 1 for ind, i in enumerate(l)}
        fs = {ind + 1: i for ind, i in enumerate(l)}
        n = len(s)
        # 2. 建树
        segtree = MaxSegTree()  # 这里因为初始值都是0， 所以不用 BUILD
        # 3. update
        for build in buildings:
            segtree.update(s[build[0]], s[build[1]] - 1, build[2], 1, n, 1)
        # 4. query
        lres = []
        for i in range(1, n + 1):
            h = segtree.query(i, i, 1, n, 1)
            if not lres or h != lres[-1][-1]:
                lres.append([fs[i], h])
        return lres


if __name__ == '__main__':
    print(
        Solution().getSkyline(
            # [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
            [[0, 2, 3], [2, 5, 3]]
        )
    )
