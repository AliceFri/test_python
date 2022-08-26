"""
Easy

输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        dp = [0] * len(nums)  # 1. 建立空间
        iSum = nums[0]  # 2. 初始值
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])  # 3. 递推公式
            iSum = max(dp[i], iSum)

        return iSum


if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
