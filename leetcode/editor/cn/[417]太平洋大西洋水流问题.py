# 有一个 m × n 的矩形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。 
# 
#  这个岛被分割成一个由若干方形单元格组成的网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标 (r, c) 上
# 单元格 高于海平面的高度 。 
# 
#  岛上雨水较多，如果相邻单元格的高度 小于或等于 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。 
# 
#  返回 网格坐标 result 的 2D列表 ，其中 result[i] = [ri, ci] 表示雨水可以从单元格 (ri, ci) 流向 太平洋和大西洋
#  。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# 输出: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
#  
# 
#  示例 2： 
# 
#  
# 输入: heights = [[2,1],[1,2]]
# 输出: [[0,0],[0,1],[1,0],[1,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == heights.length 
#  n == heights[r].length 
#  1 <= m, n <= 200 
#  0 <= heights[r][c] <= 10⁵ 
#  
#  Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 👍 419 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
from typing import List, Tuple, Set


class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def bfs(starts):
            q = deque(starts)
            v = set(starts)
            while q:
                x, y = q.popleft()
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    if heights[nx][ny] < heights[x][y]:
                        continue
                    if (nx, ny) in v:
                        continue
                    q.append((nx, ny))
                    v.add((nx, ny))
            return v

        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m - 1)]
        return list(map(list, bfs(pacific) & bfs(atlantic)))
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))