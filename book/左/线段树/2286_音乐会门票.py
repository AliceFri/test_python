# from collections import defaultdict
# from typing import List
#
#
# class BookMyShow:
#
#     def __init__(self, n: int, m: int):
#         self.m = m  # 一排 m 个 座位
#         self.n = n  # n 排
#         self.nums = [0] * (m * n + 1)   # 0 代表空位， 1 代表被占位
#         _max = len(self.nums)
#         self.tr = defaultdict(int)
#         self.up = defaultdict(int)
#         self._sum = 0
#
#     def get_ids(self, x, y):
#         return (x * self.m) + y + 1
#
#     def pushdown(self, rt, il, ir):
#         if self.up[rt]:
#             self.tr[rt << 1] = self.up[rt] * il
#             self.up[rt << 1] = self.up[rt]
#             self.tr[rt << 1 | 1] = self.up[rt] * ir
#             self.up[rt << 1 | 1] = self.up[rt]
#             self.up[rt] = 0
#
#     def update(self, L, R, C, l, r, rt):
#         if l >= L and r <= R:
#             self.tr[rt] = (r - l + 1) * C
#             self.up[rt] = C
#             return
#         mid = l + ((r - l) >> 1)
#         self.pushdown(rt, mid - l + 1, r - mid)
#         if mid >= L and l <= R:
#             self.update(L, R, C, l, mid, rt << 1)
#         if r >= L and mid + 1 <= R:
#             self.update(L, R, C, mid + 1, r, rt << 1 | 1)
#         self.tr[rt] = self.tr[rt << 1] + self.tr[rt << 1 | 1]
#
#     def query(self, L, R, l, r, rt):
#         if l >= L and r <= R:
#             return self.tr[rt]
#         mid = l + ((r - l) >> 1)
#         self.pushdown(rt, mid - l + 1, r - mid)
#         icnt = 0
#         if mid >= L and l <= R:
#             icnt += self.query(L, R, l, mid, rt << 1)
#         if r >= L and mid + 1 <= R:
#             icnt += self.query(L, R, mid + 1, r, rt << 1 | 1)
#         return icnt
#
#     def gather(self, k: int, maxRow: int) -> List[int]:
#         for row in range(0, maxRow + 1):
#             for col in range()
#
#     def scatter(self, k: int, maxRow: int) -> bool:
#
# # Your BookMyShow object will be instantiated and called as such:
# # obj = BookMyShow(n, m)
# # param_1 = obj.gather(k,maxRow)
# # param_2 = obj.scatter(k,maxRow)
from typing import List


# from collections import defaultdict
# from typing import List
#
#
class BookMyShow:

    def __init__(self, n: int, m: int):
        self.m = m  # 一排 m 个 座位
        self.n = n  # n 排
        self.start_row = 0
        self.free = [0] * (n + 1)
        self._max = [m] * (n + 1)
        self._sum = [0] * (n + 1)
        for i in range(1, n + 1):
            self.add(i, m)

    def lowbit(self, x):
        return x & -x

    def add(self, x, iadd):
        self.free[x] += iadd
        tmp = self.free[x]
        while 1 <= x <= self.m:
            self._sum[x] += iadd
            self._max[x] = max(self._max[x], tmp)
            x += self.lowbit(x)

    def query(self, x):
        icnt = 0
        while 1 <= x <= self.m:
            icnt += self._sum[x]
            x -= self.lowbit(x)
        return icnt

    def query_max(self, x, y):
        ans = 0
        while x <= y:
            ans = max(ans, self.free[y])
            y -= 1
            while x <= (y - self.lowbit(y) + 1):
                ans = max(ans, self._max[y])
                y -= self.lowbit(y)
        return ans


    def get_free(self, row):
        if row not in self.row_free:
            self.row_free[row] = self.m
        return self.row_free[row]

    def gather(self, k: int, maxRow: int) -> List[int]:
        if maxRow < self.start_row:
            return []
        if k > self.m:
            return []
        for row in range(self.start_row, maxRow + 1):
            ifree = self.get_free(row)
            if ifree >= k:
                self.row_free[row] -= k
                if row == self.start_row and self.row_free[row] == 0:
                    self.start_row += 1
                self.free -= k
                return [row, self.m - ifree]
        return []

    def scatter(self, k: int, maxRow: int) -> bool:
        return False
