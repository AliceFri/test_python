# jump = [2, 5, 1, 1, 1, 1]   3

# 通过用例 40/41 可惜
from typing import List


class Solution:
    def minJump(self, jump: List[int]) -> int:
        m = len(jump)
        _mins = [100000] * (4 * m)  # -1 代表没有设置

        def _pushdown(rt):
            if _mins[rt] != 100000:
                _mins[rt << 1] = min(_mins[rt], _mins[rt << 1])
                _mins[rt << 1 | 1] = min(_mins[rt], _mins[rt << 1 | 1])
                _mins[rt] = 100000

        def _update(L, R, C, l, r, rt):
            if l == r:
                _mins[rt] = min(_mins[rt], C)
                return
            if l >= L and r <= R:
                if C <= _mins[rt]:
                    _mins[rt] = C
                    return
            _pushdown(rt)
            mid = l + ((r - l) >> 1)
            if l <= R and mid >= L:
                _update(L, R, C, l, mid, rt << 1)
            if mid + 1 <= R and r >= L:
                _update(L, R, C, mid + 1, r, rt << 1 | 1)

        def _get(L, R, l, r, rt):
            if l == r:
                return _mins[rt]
            ires = 100000
            mid = l + ((r - l) >> 1)
            _pushdown(rt)
            if l <= R and mid >= L:
                ires = min(ires, _get(L, R, l, mid, rt << 1))
            if mid + 1 <= R and r >= L:
                ires = min(ires, _get(L, R, mid + 1, r, rt << 1 | 1))
            return ires

        res = 100000
        # 第一个位置设置成 0 步
        _update(1, 1, 0, 1, m, 1)

        for i in range(len(jump)):
            im = _get(i + 1, i + 1, 1, m, 1)
            if i + jump[i] >= len(jump):
                res = min(res, im + 1)
            ia = i + jump[i] + 1
            _update(ia, ia, im + 1, 1, m, 1)
            _update(i + 1, ia - 1, im + 2, 1, m, 1)
        return res


if __name__ == '__main__':
    print(Solution().minJump([2, 5, 1, 1, 1, 1]))
    print(
        Solution().minJump(
            [
                4,
                3,
                4,
                4,
                4,
                4,
                2,
                2,
                5,
                1,
                5,
                3,
                4,
                1,
                1,
                1,
                3,
                3,
                3,
                5,
                1,
                5,
                5,
                2,
                1,
                4,
                2,
                5,
                4,
                1,
                3,
                1,
                1,
                3,
                1,
                2,
                1,
                1,
                5,
                3,
                1,
                4,
                4,
                5,
                1,
                3,
                5,
                3,
                4,
                2,
            ]
        )
    )
    print(Solution().minJump([1] * 10000))
