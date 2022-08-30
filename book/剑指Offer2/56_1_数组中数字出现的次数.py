"""
Mid

一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
"""
from typing import List

"""
分组异或
"""
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:

        ret = 0
        for i in nums:
            ret ^= i

        div = 1
        while ret & div == 0:
            div = div << 1

        a, b = 0, 0
        for i in nums:
            if div & i:
                a ^= i
            else:
                b ^= i

        return [a, b]

"""
出现1次 和 m次数的 统一解法
"""
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1
        res, m = 0, 3
        for i in range(32):
            res <<= 1
            res |= counts[31 - i] % m
        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)