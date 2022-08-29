"""
Mid
"""
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]

        dp[0][0] = grid[0][0]
        for a in range(1, len(grid)):
            dp[a][0] = grid[a][0] + dp[a - 1][0]
        for b in range(1, len(grid[0])):
            dp[0][b] = grid[0][b] + dp[0][b - 1]

        for a in range(1, len(grid)):
            for b in range(1, len(grid[0])):
                dp[a][b] = max(dp[a - 1][b], dp[a][b - 1]) + grid[a][b]

        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().maxValue([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
