import collections


def nextGreaterElement(nums):
    lRes = [0] * len(nums)
    stack = []      # append() 和 pop(-1)

    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop(-1)

        lRes[i] = -1 if not stack else stack[-1]
        stack.append(nums[i])

    return lRes


if __name__ == '__main__':
    print(nextGreaterElement([2, 1, 2, 4, 3]))


from collections import defaultdict


# tree直接用dict 省去离散化步骤
class BIT1:
    """单点修改"""

    def __init__(self, n: int):
        self.size = n
        self.tree = defaultdict(int)

    @staticmethod
    def _lowbit(index: int) -> int:
        return index & -index

    def add(self, index: int, delta: int) -> None:
        if index <= 0:
            raise ValueError('index 必须是正整数')
        while index <= self.size:
            self.tree[index] += delta
            index += self._lowbit(index)

    def query(self, index: int) -> int:
        if index > self.size:
            index = self.size
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self._lowbit(index)
        return res

    def sumRange(self, left: int, right: int) -> int:
        return self.query(right) - self.query(left - 1)

if __name__ == '__main__':
    b1 = BIT1(10)
    pass


class BIT2:
    """范围修改"""

    def __init__(self, n: int):
        self.size = n
        self._tree1 = defaultdict(int)
        self._tree2 = defaultdict(int)

    @staticmethod
    def _lowbit(index: int) -> int:
        return index & -index

    def add(self, left: int, right: int, delta: int) -> None:
        """闭区间[left, right]加delta"""
        self._add(left, delta)
        self._add(right + 1, -delta)

    def query(self, left: int, right: int) -> int:
        """闭区间[left, right]的和"""

        return self._query(right) - self._query(left - 1)

    def _add(self, index: int, delta: int) -> None:
        if index <= 0:
            raise ValueError('index 必须是正整数')

        rawIndex = index
        while index <= self.size:
            self._tree1[index] += delta
            self._tree2[index] += (rawIndex - 1) * delta
            index += self._lowbit(index)

    def _query(self, index: int) -> int:
        if index > self.size:
            index = self.size

        rawIndex = index
        res = 0
        while index > 0:
            res += rawIndex * self._tree1[index] - self._tree2[index]
            index -= self._lowbit(index)
        return res