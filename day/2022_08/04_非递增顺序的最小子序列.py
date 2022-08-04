from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        i = 0
        nums.sort(key=lambda x: -x)
        res = []
        for a in nums:
            res.append(a)
            i += a
            if i * 2 > s:
                return res
        return nums
