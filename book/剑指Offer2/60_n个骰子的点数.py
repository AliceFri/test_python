"""
Mid

计算骰子和的概率
"""
from functools import cache
from typing import List


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        @cache
        def _dices(n):
            if n == 1:
                return {i: 1 / 6 for i in range(1, 7)}
            d = _dices(n - 1)
            nd = {}
            for k, r in d.items():
                for i in range(1, 7):
                    nd.setdefault(k + i, 0)
                    nd[k + i] += r * 1 / 6
            return nd

        res = []
        d = _dices(n)
        for i in range(n, 6 * n + 1):
            res.append(d[i])
        return res


if __name__ == '__main__':
    print(Solution().dicesProbability(11))
