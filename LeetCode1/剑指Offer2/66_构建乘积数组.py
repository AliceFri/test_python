"""
Mid

不能使用除法
"""
import functools
from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        # s = functools.reduce(lambda x, y: x * y, a)
        # ans = []
        # for i in a:
        #     ans.append(s // i)
        #
        # return ans
        # @functools.cache
        # def _fz(t):
        #     t = t.split(',')
        #     t = [int(i) for i in t]
        #     if len(t) == 1:
        #         return a[t[0]]
        #
        #     nt = [f'{t[i]}' for i in range(len(t)) if i > 0]
        #     nt = ','.join(nt)
        #     return a[t[0]] * _fz(nt)
        #
        # l = [i for i in range(0, len(a))]
        #
        # ans = []
        # for i in range(len(a)):
        #     nt = [f'{l[_i]}' for _i in range(len(l)) if _i != i]
        #     nt = ','.join(nt)
        #     ans.append(_fz(nt))
        #
        # return ans

        # if not a:
        #     return []
        # # 動態規劃
        # dp = [[] for i in range(len(a))]
        # dp[0].append(a[0])
        #
        # for i in range(1, len(a)):
        #     dp[i] =

        # 回溯法
        # ans = {}
        #
        # def _dfs(i, used, tmp):
        #     if i >= len(a):
        #         ans[used] = tmp
        #         return
        #     if i == len(a) - 1:
        #         if used == -1:
        #             _dfs(i + 1, i, tmp)
        #             return
        #     if used != -1:
        #         _dfs(i + 1, used, tmp * a[i])
        #         return
        #     _dfs(i + 1, used, tmp * a[i])
        #     _dfs(i + 1, i, tmp)
        #
        # _dfs(0, -1, 1)
        # # print(ans)
        # return [ans[i] for i in range(0, len(a))]

        # 前綴和思想
        if not a:
            return []

        L = [1 for _ in range(0, len(a))]
        R = [1 for _ in range(0, len(a))]
        L[0] = 1
        R[-1] = 1

        for i in range(1, len(a)):
            L[i] = a[i - 1] * L[i - 1]
        for i in range(len(a) - 2, -1, -1):
            R[i] = R[i + 1] * a[i + 1]

        ans = [L[i] * R[i] for i in range(0, len(a))]
        return ans


if __name__ == "__main__":
    print(Solution().constructArr([1, 2, 3, 4, 5]))
