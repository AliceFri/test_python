"""
给你一个整数数组 nums ，按要求返回一个新数组 counts 。数组 counts 有该性质： counts[i] 的值是 nums[i] 右侧小于 nums[i] 的元素的数量。
"""
from typing import List
from collections import defaultdict


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # 1. 离散化
        l = sorted(list(set(nums)))
        l = l[::-1]
        s = {ind + 1: i for ind, i in enumerate(l)}
        fs = {i: ind + 1 for ind, i in enumerate(l)}

        # 2. 线段树定义
        _nums = defaultdict(int)
        _laze = defaultdict(int)

        def _push_down(rt, ln, rn):
            if _laze[rt]:
                _nums[rt << 1] += _laze[rt] * ln
                _nums[rt << 1 | 1] += _laze[rt] * rn
                _laze[rt << 1] += _laze[rt]
                _laze[rt << 1 | 1] += _laze[rt]
                _laze[rt] = 0

        def _push_up(rt):
            _nums[rt] = _nums[rt << 1] + _nums[rt << 1 | 1]

        def _add(L, R, C, l, r, rt):
            if l >= L and r <= R:
                _nums[rt] += (r - l + 1) * C
                _laze[rt] += C
                return
            mid = l + ((r - l) >> 1)
            _push_down(rt, mid - l + 1, r - mid)
            if l <= R and mid >= L:
                _add(L, R, C, l, mid, rt << 1)
            if mid + 1 <= R and r >= L:
                _add(L, R, C, mid + 1, r, rt << 1 | 1)
            _push_up(rt)

        def _query(L, R, l, r, rt):
            if l >= L and r <= R:
                return _nums[rt]
            mid = l + ((r - l) >> 1)
            _push_down(rt, mid - l + 1, r - mid)
            cnt = 0
            if l <= R and mid >= L:
                cnt += _query(L, R, l, mid, rt << 1)
            if mid + 1 <= R and r >= L:
                cnt += _query(L, R, mid + 1, r, rt << 1 | 1)
            return cnt

        count = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            k = nums[i]
            q = _query(fs[k] + 1, len(s), 1, len(s), 1)
            count[i] = q
            _add(fs[k], fs[k], 1, 1, len(s), 1)

        return count


if __name__ == '__main__':
    print(Solution().countSmaller([5, 2, 6, 1]))
    print(Solution().countSmaller([-1]))
    print(Solution().countSmaller([-1, 0]))

