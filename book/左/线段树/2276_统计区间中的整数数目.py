# 1 <= left <= right <= 109
from collections import defaultdict


class CountIntervals:
    def __init__(self):
        self.nums = defaultdict(int)
        self.upd = defaultdict(int)

    def pushdown(self, rt, ln, rn):
        if self.upd[rt]:
            self.nums[rt << 1] = self.upd[rt] * ln
            self.upd[rt << 1] = self.upd[rt]
            self.nums[rt << 1 | 1] = self.upd[rt] * rn
            self.upd[rt << 1 | 1] = self.upd[rt]
            self.upd[rt] = 0

    def update(self, L, R, C, l, r, rt):
        if l >= L and r <= R:
            self.nums[rt] = C * (r - l + 1)
            self.upd[rt] = C
            return
        mid = l + ((r - l) >> 1)
        self.pushdown(rt, mid - l + 1, r - mid)
        if mid >= L and l <= R:
            self.update(L, R, C, l, mid, rt << 1)
        if r >= L and mid + 1 <= R:
            self.update(L, R, C, mid + 1, r, rt << 1 | 1)
        self.nums[rt] = self.nums[rt << 1] + self.nums[rt << 1 | 1]

    def query(self, L, R, l, r, rt):
        if l >= L and r <= R:
            return self.nums[rt]
        mid = l + ((r - l) >> 1)
        self.pushdown(rt, mid - l + 1, r - mid)
        icnt = 0
        if mid >= L and l <= R:
            icnt += self.query(L, R, l, mid, rt << 1)
        if r >= L and mid + 1 <= R:
            icnt += self.query(L, R, mid + 1, r, rt << 1 | 1)
        return icnt

    def add(self, left: int, right: int) -> None:
        self.update(left, right, 1, 1, 10**9, 1)

    def count(self) -> int:
        return self.query(1, 10**9, 1, 10**9, 1)


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
if __name__ == '__main__':
    obj = CountIntervals()
    obj.add(2, 3)
    print(obj.count())
    obj.add(7, 10)
    print(obj.count())
    obj.add(5, 8)
    print(obj.count())


class CountIntervals:
    __slots__ = 'left', 'right', 'l', 'r', 'cnt'

    def __init__(self, l=1, r=10**9):
        self.left = self.right = None
        self.l, self.r, self.cnt = l, r, 0

    def add(self, l: int, r: int) -> None:
        if self.cnt == self.r - self.l + 1:
            return  # self 已被完整覆盖，无需执行任何操作
        if l <= self.l and self.r <= r:  # self 已被区间 [l,r] 完整覆盖，不再继续递归
            self.cnt = self.r - self.l + 1
            return
        mid = (self.l + self.r) // 2
        if self.left is None:
            self.left = CountIntervals(self.l, mid)  # 动态开点
        if self.right is None:
            self.right = CountIntervals(mid + 1, self.r)  # 动态开点
        if l <= mid:
            self.left.add(l, r)
        if mid < r:
            self.right.add(l, r)
        self.cnt = self.left.cnt + self.right.cnt

    def count(self) -> int:
        return self.cnt


from sortedcontainers import SortedDict


class CountIntervals:
    def __init__(self):
        self.d = SortedDict()
        self.cnt = 0  # 所有区间长度和

    def add(self, left: int, right: int) -> None:
        # 遍历所有被 [left,right] 覆盖到的区间（部分覆盖也算）
        i = self.d.bisect_left(left)
        while i < len(self.d) and self.d.values()[i] <= right:
            r, l = self.d.items()[i]
            left = min(left, l)  # 合并后的新区间，其左端点为所有被覆盖的区间的左端点的最小值
            right = max(right, r)  # 合并后的新区间，其右端点为所有被覆盖的区间的右端点的最大值
            self.cnt -= r - l + 1
            self.d.popitem(i)
        self.cnt += right - left + 1
        self.d[right] = left  # 所有被覆盖到的区间与 [left,right] 合并成一个新区间

    def count(self) -> int:
        return self.cnt
