# 在 n x n 的网格 grid 中，我们放置了一些与 x，y，z 三轴对齐的 1 x 1 x 1 立方体。 
# 
#  每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。 
# 
#  现在，我们查看这些立方体在 xy 、yz 和 zx 平面上的投影。 
# 
#  投影 就像影子，将 三维 形体映射到一个 二维 平面上。从顶部、前面和侧面看立方体时，我们会看到“影子”。 
# 
#  返回 所有三个投影的总面积 。 
# 
#  
# 
#  
#  
# 
#  
#  
# 
#  
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：[[1,2],[3,4]]
# 输出：17
# 解释：这里有该形体在三个轴对齐平面上的三个投影(“阴影部分”)。
#  
# 
#  示例 2: 
# 
#  
# 输入：grid = [[2]]
# 输出：5
#  
# 
#  示例 3： 
# 
#  
# 输入：[[1,0],[0,2]]
# 输出：8
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == grid.length == grid[i].length 
#  1 <= n <= 50 
#  0 <= grid[i][j] <= 50 
#  
#  Related Topics 几何 数组 数学 矩阵 👍 108 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def projectionArea(self, grid) -> int:
        # 三个方向
        # 正面
        area1 = sum(map(max, grid))

        area2 = 0
        for i in range(len(grid[0])):
            area2 += max([grid[a][i] for a in range(len(grid))])

        area3 = 0
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if grid[a][b]:
                    area3 += 1

        return area1 + area2 + area3
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().projectionArea([[1, 0], [0, 2]]))
