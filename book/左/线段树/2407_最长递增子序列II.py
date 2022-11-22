# nums = [4,2,1,4,3,4,5,8,15], k = 3 ans = 5
# [7,4,5,1,8,12,4,7], k = 5 ans 4
# [1, 5] k = 1 ans = 1
from typing import List
from collections import defaultdict


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        l = set(nums)
        for i in nums:
            l.add(i + k)
        l = list(l)
        l.sort()
        s = {i: ind + 1 for ind, i in enumerate(l)}
        d, n, res = {}, len(s), 0
        dps = [0] * (4 * n + 1)
        ups = [0] * (4 * n + 1)

        def _pushdown(rt):
            if ups[rt]:
                dps[rt << 1] = ups[rt]
                ups[rt << 1] = ups[rt]
                dps[rt << 1 | 1] = ups[rt]
                ups[rt << 1 | 1] = ups[rt]
                ups[rt] = 0

        def _update(L, R, C, l, r, rt):
            if l >= L and r <= R:
                dps[rt] = C
                ups[rt] = C
                return
            mid = l + ((r - l) >> 1)
            _pushdown(rt)
            if l <= R and mid >= L:
                _update(L, R, C, l, mid, rt << 1)
            if mid + 1 <= R and r >= L:
                _update(L, R, C, mid + 1, r, rt << 1 | 1)
            dps[rt] = max(dps[rt << 1], dps[rt << 1 | 1])

        def _query(L, R, l, r, rt):
            if l >= L and r <= R:
                return dps[rt]
            mid = l + ((r - l) >> 1)
            _pushdown(rt)
            imax = 0
            if l <= R and mid >= L:
                imax = max(imax, _query(L, R, l, mid, rt << 1))
            if mid + 1 <= R and r >= L:
                imax = max(imax, _query(L, R, mid + 1, r, rt << 1 | 1))
            return imax

        for i in nums[::-1]:
            tmp = _query(s[i] + 1, s[i + k], 1, n, 1) + 1
            res = max(tmp, res)
            _update(s[i], s[i], tmp, 1, n, 1)
        return res


if __name__ == '__main__':
    print(Solution().lengthOfLIS([4, 2, 1, 4, 3, 4, 5, 8, 15], 3))
    print(Solution().lengthOfLIS([7, 3, 5, 1, 8, 12, 3, 7], 5))
    print(Solution().lengthOfLIS([1, 5], 1))
