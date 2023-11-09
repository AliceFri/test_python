from typing import List
from collections import deque
import heapq


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        h = []

        def getids(x, y):
            return x * n + y

        dp = [[-1] * (m * n) for _ in range(m * n)]
        for i in range(m * n):
            dp[i][i] = 0
        for a in range(m):
            for b in range(n):
                if not forest[a][b]:
                    continue
                if forest[a][b] > 1:
                    h.append((forest[a][b], getids(a, b)))
                for a1, b1 in moves:
                    na, nb = a + a1, b + b1
                    if 0 <= na < m and 0 <= nb < n and forest[na][nb]:
                        dp[getids(a, b)][getids(na, nb)] = 1
                        dp[getids(na, nb)][getids(a, b)] = 1

        # 多源最短路径 这里要换成 BFS
        # for k in range(m * n):
        #     for a in range(m * n):
        #         for b in range(m * n):
        #             if dp[a][k] != -1 and dp[k][b] != -1:
        #                 if dp[a][b] == -1:
        #                     dp[a][b] = dp[a][k] + dp[k][b]
        #                 else:
        #                     dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])
        def bfs(x, y):
            ids = getids(x, y)
            visited = set()
            visited.add((x, y))
            q = deque()
            q.append((x, y, 0))
            while q:
                x, y, dis = q.popleft()
                dp[ids][getids(x, y)] = dis
                for a1, b1 in moves:
                    na, nb = x + a1, y + b1
                    if (
                        0 <= na < m
                        and 0 <= nb < n
                        and forest[na][nb]
                        and (na, nb) not in visited
                    ):
                        visited.add((na, nb))
                        q.append((na, nb, dis + 1))

        for a in range(m):
            for b in range(n):
                if forest[a][b] > 1:
                    bfs(a, b)

        h.sort()

        curids = 0
        res = 0
        for _, ids in h:
            if dp[curids][ids] == -1:
                return -1
            res += dp[curids][ids]
            curids = ids
        return res


if __name__ == '__main__':
    print(
        Solution().cutOffTree(
            [
                [54581641, 64080174, 24346381, 69107959],
                [86374198, 61363882, 68783324, 79706116],
                [668150, 92178815, 89819108, 94701471],
                [83920491, 22724204, 46281641, 47531096],
                [89078499, 18904913, 25462145, 60813308],
            ]
        )
    )
