from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        m, n = len(mat), len(mat[0])

        a, b = 0, 0
        path = 1  # path 为 1, (-1, +1) -1: (+1, -1)

        def getNAB(a, b):
            nonlocal path
            if path == 1:
                na, nb = a - 1, b + 1
            else:
                na, nb = a + 1, b - 1

            if 0 <= na < m and 0 <= nb < n:
                return na, nb

            if path == 1:
                path = -path
                if b < n - 1:
                    return a, b + 1
                return a + 1, b
            else:
                path = -path
                if a < m - 1:
                    return a + 1, b
                return a, b + 1

        ret = []
        for i in range(m * n):
            # print(a, b, path)
            ret.append(mat[a][b])
            a, b = getNAB(a, b)

        return ret
