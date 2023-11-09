"""

统计一个数字在排序数组中出现的次数。
"""
from typing import List

"""
找到最左边的下标， 找到最右边的下标 相减
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_left():
            a, b = 0, len(nums) - 1
            res = -1
            while a <= b:
                m = a + (b - a) // 2
                if nums[m] < target:
                    a = m + 1
                elif nums[m] > target:
                    b = m - 1
                else:
                    res = m
                    b = m - 1
            return res

        def find_right():
            a, b = 0, len(nums) - 1
            res = -1
            while a <= b:
                m = a + (b - a) // 2
                if nums[m] < target:
                    a = m + 1
                elif nums[m] > target:
                    b = m - 1
                else:
                    res = m
                    a = m + 1
            return res

        i1 = find_left()
        if i1 == -1:
            return 0
        return find_right() - i1 + 1


if __name__ == '__main__':
    print(Solution().search([5, 7, 7, 8, 8, 10], 6))
