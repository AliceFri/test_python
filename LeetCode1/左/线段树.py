"""
[1, 2, 3, 7, 6, 4, ...]

void add(L, R, v)   从 L 到 R 范围， 加上 v

void update(L, R, v)    从 L 到 R 范围， 变成 v

void getSum(L, R)       从 L 到 R， 求和

"""


class SegTree:
    def __init__(self, arr):
        self.arr = [0] + arr[:]  # 下标 0 不用， 方便使用 位运算

        self._sum = [0] * (len(self.arr) << 2)  # 范围 * 4, 满二叉树需要的最大范围
        self.laze = [0] * (len(self.arr) << 2)  # 存 范围增加范围的 信息
        self.update = [0] * (len(self.arr) << 2)
        self.change = [0] * (len(self.arr) << 2)

    def build(self, il, ir, rt):
        """
        将 【il ~ ir】 范围的数， 填到 rt 位置上
        """
        if il == ir:
            self._sum[rt] = self.arr[il]
            return self._sum[rt]
        im = il + ((ir - il) // 2)
        self.build(il, im, rt << 1)
        self.build(im + 1, ir, (rt << 1) | 1)
        self.pushUp(rt)
        # self._sum[rt] = a1 + a2
        # return self._sum[rt]

    def add(self, L, R, C, l, r, rt):
        """
        L..R 任务范围， 所有的值 累加上 C
        l, r 当前表达的范围
        rt, l .. r 范围上的 位置
        """
        # 任务的范围 覆盖了 表达范围 不下发
        if L <= l and r <= R:
            self._sum[rt] += C * (r - l + 1)
            self.laze[rt] += C
            return
        # 任务 没有 把当前范围 包住， 需要下发
        mid = l + ((r - l) >> 1)
        self.pushDown(rt, mid - l + 1, r - mid)
        if mid >= L and l <= R:
            self.add(L, R, C, l, mid, rt << 1)
        if r >= L and mid + 1 <= R:
            self.add(L, R, C, mid + 1, r, rt << 1 | 1)
        self.pushUp(rt)

    def pushDown(self, rt, ln, rn):
        """
        ln 左子树结点数， rn 右子数结点数， rt 当前结点
        """
        if self.update[rt]:
            self.update[rt << 1] = 1
            self.update[rt << 1 | 1] = 1
            self.change[rt << 1] = self.change[rt]
            self.change[rt << 1 | 1] = self.change[rt]
            self.laze[rt << 1] = 0
            self.laze[rt << 1 | 1] = 0
            self._sum[rt << 1] = self.change[rt] * ln
            self._sum[rt << 1 | 1] = self.change[rt] * rn
            self.update[rt] = 0
        if self.laze[rt] != 0:
            self.laze[rt << 1] += self.laze[rt]
            self._sum[rt << 1] += self.laze[rt] * ln
            self.laze[rt << 1 | 1] += self.laze[rt]
            self._sum[rt << 1 | 1] += self.laze[rt] * rn
            self.laze[rt] = 0

    def pushUp(self, rt):
        self._sum[rt] = self._sum[rt << 1] + self._sum[rt << 1 | 1]

    def func_update(self, L, R, C, l, r, rt):
        """
        L..R 任务范围， 所有的值 累加上 C
        l, r 当前表达的范围
        rt, l .. r 范围上的 位置
        """
        # print(l, r, rt)
        if L <= l and r <= R:
            self.update[rt] = 1
            self.change[rt] = C
            self.laze[rt] = 0
            self._sum[rt] = (r - l + 1) * C
            return
        mid = l + ((r - l) >> 1)
        self.pushDown(rt, mid - l + 1, r - mid)
        if l <= R and mid >= L:
            self.func_update(L, R, C, l, mid, rt << 1)
        if mid + 1 <= R and r >= L:
            self.func_update(L, R, C, mid + 1, r, rt << 1 | 1)
        self.pushUp(rt)

    def query(self, L, R, l, r, rt):
        if L <= l and r <= R:
            return self._sum[rt]
        mid = l + ((r - l) >> 1)
        self.pushDown(rt, mid - l + 1, r - mid)
        ans = 0
        if l <= R and mid >= L:
            ans += self.query(L, R, l, mid, rt << 1)
        if mid + 1 <= R and r >= L:
            ans += self.query(L, R, mid + 1, r, rt << 1 | 1)
        return ans

    @property
    def sum(self):
        return self._sum


def print_s(s):
    print(
        s.query(1, 4, 1, 4, 1),
        (
            s.query(1, 1, 1, 4, 1),
            s.query(2, 2, 1, 4, 1),
            s.query(3, 3, 1, 4, 1),
            s.query(4, 4, 1, 4, 1),
        ),
        s.query(2, 3, 1, 4, 1),
    )


def show_s(s):
    print(s.sum)
    print('laze:', s.laze)
    print('update:', s.update)
    print('change:', s.change)


if __name__ == "__main__":
    s = SegTree([4, 3, 5, 2])
    s.build(1, 4, 1)
    # s.func_update(1, 3, 1, 1, 4, 1)  # 1, 1, 1 , 2
    # print_s(s)
    # show_s(s)
    # s.func_update(2, 3, 2, 1, 4, 1)  # 1, 2, 2 , 2
    # print_s(s)
    # show_s(s)
    s.add(1, 1, 10, 1, 4, 1)  # 3, 4, 2, 2
    print_s(s)
    show_s(s)
    # print(s.query(1, 4, 1, 4, 1))
    # print(s.query(1, 1, 1, 4, 1))
    # print(s.query(2, 2, 1, 4, 1))
    # print(s.query(3, 3, 1, 4, 1))
    # print(s.query(4, 4, 1, 4, 1))
    # print(s.query(2, 3, 1, 4, 1))
