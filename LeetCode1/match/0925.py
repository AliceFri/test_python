# 6191. 好路径的数目
# 123 / 131 个通过测试用例


from functools import cache
import sys
from typing import List

sys.setrecursionlimit(100000)


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        d = {}
        for i in range(len(vals)):
            d.setdefault(vals[i], [])
            d[vals[i]].append(i)

        paths = {}
        for p in edges:
            p0, p1 = p
            paths.setdefault(p0, [])
            paths.setdefault(p1, [])
            paths[p0].append(p1)
            paths[p1].append(p0)

        ires = len(vals)

        def __max(a, b):
            if a == 1000000:
                return b
            if b == 1000000:
                return a
            return max(a, b)

        def __min(a, b):
            if a == 1000000:
                return b
            if b == 1000000:
                return a
            return min(a, b)

        @cache
        def _max(a, b, pre=None):
            if a == b:
                return vals[a]
            l = paths[a]
            if len(l) == 1:
                if pre != l[0]:
                    return __max(vals[a], _max(l[0], b, a))
                return 1000000
            _ret = vals[a]
            _m = 100000
            for i in l:
                if i == pre:
                    continue
                _m = __min(_m, _max(i, b, a))
            return __max(_ret, _m)

        for k in d.keys():
            if len(d[k]) < 2:
                continue
            for a in range(0, len(d[k]) - 1):
                for b in range(a + 1, len(d[k])):
                    _a, _b = d[k][a], d[k][b]
                    if _max(_a, _b) <= k:
                        ires += 1

        return ires


if __name__ == "__main__":
    print(
        Solution().numberOfGoodPaths(
            vals=[2, 4, 1, 2, 2, 5, 3, 4, 4],
            edges=[[0, 1], [2, 1], [0, 3], [4, 1], [4, 5], [3, 6], [7, 5], [2, 8]],
        )
    )
