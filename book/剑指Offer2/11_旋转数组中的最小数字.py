"""
Easy

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

给你一个可能存在 重复 元素值的数组 numbers ，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。请返回旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为 1。
"""
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        a, b = 0, len(numbers) - 1
        while a < b:
            m = ((b - a) >> 1) + a

            if numbers[m] > numbers[b]:
                a = m + 1
            elif numbers[m] < numbers[b]:
                b = m
            else:
                b -= 1
        assert a == b
        return numbers[a]


if __name__ == '__main__':
    print(Solution().minArray([3, 4, 5, 1, 2]))
    print(Solution().minArray([2, 2, 2, 2, 2]))
