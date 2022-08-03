import collections
from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        # 前缀和

        res = [0] * len(positions)

        for i, (left, height) in enumerate(positions):
            res[i] = height

            for a in range(i):
                if left < positions[a][0] + positions[a][1] and left + height > positions[a][0]:
                    res[i] = max(res[i], res[a] + height)

        for i in range(len(positions) - 1):
            res[i + 1] = max(res[i], res[i + 1])

        return res