"""
Easy

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        side = 0  # 移动方向
        res = []

        a, b = 0, 0
        visted = set()

        for _ in range(len(matrix) * len(matrix[0])):
            res.append(matrix[a][b])
            visted.add((a, b))

            na, nb = a + move[side][0], b + move[side][1]
            if (
                na < 0
                or na >= len(matrix)
                or nb < 0
                or nb >= len(matrix[0])
                or (na, nb) in visted
            ):
                side = (side + 1) % 4
                na, nb = a + move[side][0], b + move[side][1]
            a, b = na, nb

        return res


if __name__ == '__main__':
    print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
