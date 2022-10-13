from functools import cache


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        flag = [[0] * n for _ in range(n)]

        @cache
        def get_influence_grid(x, y):
            lret = []
            for i in range(n):
                lret.append((x, i))
                lret.append((i, y))
            nx, ny = x + 1, y + 1
            while nx < n and ny < n:
                lret.append((nx, ny))
                nx, ny = nx + 1, ny + 1
            nx, ny = x - 1, y - 1
            while nx >= 0 and ny >= 0:
                lret.append((nx, ny))
                nx, ny = nx - 1, ny - 1
            nx, ny = x - 1, y + 1
            while nx >= 0 and ny < n:
                lret.append((nx, ny))
                nx, ny = nx - 1, ny + 1
            nx, ny = x + 1, y - 1
            while nx < n and ny >= 0:
                lret.append((nx, ny))
                nx, ny = nx + 1, ny - 1
            return lret

        def addflag(x, y, iflag):
            for a, b in get_influence_grid(x, y):
                flag[a][b] += iflag

        iret = 0

        def dfs(i):
            nonlocal iret
            if i >= n:
                iret += 1
                return
            for a in range(n):
                if flag[i][a] > 0:
                    continue
                addflag(i, a, 1)
                dfs(i + 1)
                addflag(i, a, -1)

        dfs(0)
        return iret


if __name__ == '__main__':
    print(Solution().totalNQueens(11))

