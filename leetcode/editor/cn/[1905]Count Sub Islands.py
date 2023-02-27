# You are given two m x n binary matrices grid1 and grid2 containing only 0's (
# representing water) and 1's (representing land). An island is a group of 1's 
# connected 4-directionally (horizontal or vertical). Any cells outside of the grid 
# are considered water cells. 
# 
#  An island in grid2 is considered a sub-island if there is an island in grid1 
# that contains all the cells that make up this island in grid2. 
# 
#  Return the number of islands in grid2 that are considered sub-islands. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], 
# grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# Output: 3
# Explanation: In the picture above, the grid on the left is grid1 and the grid 
# on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. 
# There are three sub-islands.
#  
# 
#  Example 2: 
# 
#  
# Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], 
# grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# Output: 2 
# Explanation: In the picture above, the grid on the left is grid1 and the grid 
# on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. 
# There are two sub-islands.
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid1.length == grid2.length 
#  n == grid1[i].length == grid2[i].length 
#  1 <= m, n <= 500 
#  grid1[i][j] and grid2[i][j] are either 0 or 1. 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 86 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # 1. grid2 找出所有的岛 dfs
        lands = []
        visited = set([])

        def dfs(a, b):
            s = set([(a, b)])
            visited.add((a, b))
            for i1, i2 in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                a1, b1 = a + i1, b + i2
                if 0 <= a1 < len(grid2) and 0 <= b1 < len(grid2[0]) and grid2[a1][b1] and (a1, b1) not in visited:
                    s1 = dfs(a1, b1)
                    if len(s1) > len(s):
                        s, s1 = s1, s
                    s.update(s1)
            return s

        for a in range(len(grid2)):
            for b in range(len(grid2[0])):
                if grid2[a][b] == 0:
                    continue
                if (a, b) in visited:
                    continue
                lands.append(dfs(a, b))

        icnt = 0
        for land in lands:
            c = True
            for a, b in land:
                if grid1[a][b] == 0:
                    c = False
                    break
            if c:
                icnt += 1
        return icnt
# leetcode submit region end(Prohibit modification and deletion)
