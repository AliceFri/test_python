"""
Easy

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。
"""
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        # 也可以用双指针， 这种可以说成是单指针或快慢指针
        i = 0
        for a in range(len(nums)):
            if nums[a] & 1:
                if a != i:
                    nums[a], nums[i] = nums[i], nums[a]
                i += 1

        return nums