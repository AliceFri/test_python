"""
Easy

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
"""


class MinStack:
    """
    辅助栈
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []  # 数据栈, 只支持append, pop(-1)
        self.min_index = []  # 最小栈

    def push(self, x: int) -> None:
        self.nums.append(x)
        ind = len(self.nums) - 1
        if not self.min_index or x <= self.nums[self.min_index[-1]]:
            self.min_index.append(ind)

    def pop(self) -> None:
        if not self.nums:
            return None
        ind = len(self.nums) - 1
        self.nums.pop(-1)
        if ind == self.min_index[-1]:
            self.min_index.pop(-1)

    def top(self) -> int:
        if not self.nums:
            return None
        return self.nums[-1]

    def min(self) -> int:
        if not self.min_index:
            return None
        return self.nums[self.min_index[-1]]
