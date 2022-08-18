"""
Easy 找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

[2, 3, 1, 0, 2, 5, 3] -> 2/3
[1, 1, 1] -> 1
"""
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for ind in range(len(nums)):
            i = nums[ind]

            while i != ind:
                if i < ind:
                    return i
                if nums[i] == nums[ind]:
                    return nums[i]
                nums[i], nums[ind] = nums[ind], nums[i]
                i = nums[ind]
        return -1


if __name__ == '__main__':
    print(Solution().findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
    print(Solution().findRepeatNumber([1, 1, 1]))
