"""
Easy

输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dFind = {}
        for i in nums:
            if i in dFind:
                return [i, dFind[i]]
            find = target - i
            dFind[find] = i

        return [0, 0]