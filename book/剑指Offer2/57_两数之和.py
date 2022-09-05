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

    """
    和为s的连续正数序列
    """
    """
    滑动窗口
    """
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        pre_sum = [0] * (target // 2 + 2)
        dsum = {0: 0}
        for i in range(1, len(pre_sum)):
            pre_sum[i] = i + pre_sum[i - 1]
            dsum[pre_sum[i]] = i

        res = []
        for i in range(target // 2 + 2):
            ifind = target + pre_sum[i]
            if ifind in dsum:
                iright = dsum[ifind]
                if iright > i:
                    res.append([_ for _ in range(i + 1, iright + 1)])

        return res


if __name__ == '__main__':
    print(Solution().findContinuousSequence(9))