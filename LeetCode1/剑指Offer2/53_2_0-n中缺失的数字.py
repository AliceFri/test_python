"""
Easy

"""
from typing import List

"""
有序的话用二分
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = 0
        for i in range(1, len(nums) + 1):
            a ^= i
        for i in nums:
            a ^= i
        return a


if __name__ == '__main__':
    print(Solution().missingNumber([0, 1, 3]))
