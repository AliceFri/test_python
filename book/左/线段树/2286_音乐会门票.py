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
        self.free = [m] * (n + 1)
        self._max = [m] * (n + 1)
        self._sum = [0] * (n + 1)
        self.start_row = 1
        self.used_row = 1
        for i in range(1, n + 1):
            self._sum[i] = self.lowbit(i) * self.m
        # for i in range(1, n + 1):
        #     self.add(i, m)

    def info(self):
        print("nums", self.free)
        # print("_max", self._max)
        # print("_sum", self._sum)

    def lowbit(self, x):
        return x & -x

    def add(self, x, iadd):
        self.used_row = max(x, self.used_row)
        self.free[x] += iadd
        tmp = self.free[x]
        while 1 <= x <= self.n:
            self._sum[x] += iadd
            # self._max[x] = max(self._max[x], tmp)
            self._max[x] = self.free[x]
            i = 1
            while i < self.lowbit(x):
                self._max[x] = max(self._max[x], self._max[x - i])
                i = i << 1

            x += self.lowbit(x)

    def query(self, x):
        x = min(x, self.n)
        icnt = 0
        while 1 <= x <= self.n:
            icnt += self._sum[x]
            x -= self.lowbit(x)
        return icnt

    def query_max(self, x, y):
        ans = 0
        while x <= y:
            ans = max(ans, self.free[y])
            y -= 1
            while x <= (y - self.lowbit(y)):
                ans = max(ans, self._max[y])
                y -= self.lowbit(y)
        return ans

    def gather(self, k: int, maxRow: int) -> List[int]:
        il, ih = 1, maxRow + 1
        ih = max(ih, self.used_row)
        if self.query_max(il, ih) >= k:
            while il < ih:
                im = il + ((ih - il) >> 1)
                if self.query_max(il, im) >= k:
                    ih = im
                else:
                    il = im + 1
            k1 = self.query(il) - self.query(il - 1)
            self.add(il, -k)
            return [il - 1, self.m - k1]
        return []

    def scatter(self, k: int, maxRow: int) -> bool:
        isum = self.query(maxRow + 1)
        if isum < k:
            return False
        isub = 0
        while k > 0:
            k1 = self.query(self.start_row) - self.query(self.start_row - 1)
            isub = min(k, k1)
            self.add(self.start_row, -isub)
            k -= isub
            if isub == k1:
                self.start_row += 1
        return True


# class BookMyShow:
#     def __init__(self, n: int, m: int):
#         self.n = n
#         self.m = m
#         self.min = [0] * (n * 4)
#         self.sum = [0] * (n * 4)
#
#     # 将 idx 上的元素值增加 val
#     def add(self, o: int, l: int, r: int, idx: int, val: int) -> None:
#         if l == r:
#             self.min[o] += val
#             self.sum[o] += val
#             return
#         m = (l + r) // 2
#         if idx <= m: self.add(o * 2, l, m, idx, val)
#         else: self.add(o * 2 + 1, m + 1, r, idx, val)
#         self.min[o] = min(self.min[o * 2], self.min[o * 2 + 1])
#         self.sum[o] = self.sum[o * 2] + self.sum[o * 2 + 1]
#
#     # 返回区间 [L,R] 内的元素和
#     def query_sum(self, o: int, l: int, r: int, L: int, R: int) -> int:
#         if L <= l and r <= R: return self.sum[o]
#         sum = 0
#         m = (l + r) // 2
#         if L <= m: sum += self.query_sum(o * 2, l, m, L, R)
#         if R > m: sum += self.query_sum(o * 2 + 1, m + 1, r, L, R)
#         return sum
#
#     # 返回区间 [1,R] 中 <= val 的最靠左的位置，不存在时返回 0
#     def index(self, o: int, l: int, r: int, R: int, val: int) -> int:
#         if self.min[o] > val: return 0  # 说明整个区间的元素值都大于 val
#         if l == r: return l
#         m = (l + r) // 2
#         if self.min[o * 2] <= val: return self.index(o * 2, l, m, R, val)  # 看看左半部分
#         if m < R: return self.index(o * 2 + 1, m + 1, r, R, val)  # 看看右半部分
#         return 0
#
#     def gather(self, k: int, maxRow: int) -> List[int]:
#         i = self.index(1, 1, self.n, maxRow + 1, self.m - k)
#         if i == 0: return []
#         seats = self.query_sum(1, 1, self.n, i, i)
#         self.add(1, 1, self.n, i, k)  # 占据 k 个座位
#         return [i - 1, seats]
#
#     def scatter(self, k: int, maxRow: int) -> bool:
#         if (maxRow + 1) * self.m - self.query_sum(1, 1, self.n, 1, maxRow + 1) < k:
#             return False  # 剩余座位不足 k 个
#         i = self.index(1, 1, self.n, maxRow + 1, self.m - 1)  # 从第一个没有坐满的排开始占座
#         while True:
#             left_seats = self.m - self.query_sum(1, 1, self.n, i, i)
#             if k <= left_seats:  # 剩余人数不够坐后面的排
#                 self.add(1, 1, self.n, i, k)
#                 return True
#             k -= left_seats
#             self.add(1, 1, self.n, i, left_seats)
#             i += 1
#
# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/booking-concert-tickets-in-groups/solution/by-endlesscheng-okcu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == "__main__":
    book = BookMyShow(25000, 50000)
    for i in range(10000):
        book.gather(49999, 24999)
    book.info()
    print('---------------------------')

