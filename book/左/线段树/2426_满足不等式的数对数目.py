import collections
from typing import List
from collections import defaultdict


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        num = [(nums1[i] - nums2[i]) for i in range(len(nums1))]
        s = set(num)
        for i in num:
            s.add(i - diff)
        l = list(s)
        l.sort()
        s = {i: ind + 1 for ind, i in enumerate(l)}
        n = len(s)
        dp = [0] * (n + 1)

        def _lowbit(x):
            return x & -x

        def _add(x, iadd):
            while 1 <= x <= n:
                dp[x] += iadd
                x += _lowbit(x)

        def _query(x):
            icnt = 0
            while 1 <= x <= n:
                icnt += dp[x]
                x -= _lowbit(x)
            return icnt

        ires = 0
        for i in num[::-1]:
            ires += _query(n) - _query(s[i - diff] - 1)
            _add(s[i], 1)

        return ires


if __name__ == '__main__':
    print(Solution().numberOfPairs([3, 2, 5], [2, 2, 1], 1))
    print(Solution().numberOfPairs([3, -1], [-2, 2], -1))
