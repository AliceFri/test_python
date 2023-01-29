# There is a 1-based binary matrix where 0 represents land and 1 represents 
# water. You are given integers row and col representing the number of rows and 
# columns in the matrix, respectively. 
# 
#  Initially on day 0, the entire matrix is land. However, each day a new cell 
# becomes flooded with water. You are given a 1-based 2D array cells, where cells[
# i] = [ri, ci] represents that on the iᵗʰ day, the cell on the riᵗʰ row and ciᵗʰ 
# column (1-based coordinates) will be covered with water (i.e., changed to 1). 
# 
#  You want to find the last day that it is possible to walk from the top to 
# the bottom by only walking on land cells. You can start from any cell in the top 
# row and end at any cell in the bottom row. You can only travel in the four 
# cardinal directions (left, right, up, and down). 
# 
#  Return the last day where it is possible to walk from the top to the bottom 
# by only walking on land cells. 
# 
#  
#  Example 1: 
# 
#  
# Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
# Output: 2
# Explanation: The above image depicts how the matrix changes each day starting 
# from day 0.
# The last day where it is possible to cross from top to bottom is on day 2.
#  
# 
#  Example 2: 
# 
#  
# Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
# Output: 1
# Explanation: The above image depicts how the matrix changes each day starting 
# from day 0.
# The last day where it is possible to cross from top to bottom is on day 1.
#  
# 
#  Example 3: 
# 
#  
# Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3
# ,2],[3,1]]
# Output: 3
# Explanation: The above image depicts how the matrix changes each day starting 
# from day 0.
# The last day where it is possible to cross from top to bottom is on day 3.
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= row, col <= 2 * 10⁴ 
#  4 <= row * col <= 2 * 10⁴ 
#  cells.length == row * col 
#  1 <= ri <= row 
#  1 <= ci <= col 
#  All the values of cells are unique. 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 二分查找 矩阵 👍 37 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # start, end = 0, 1
        headers = list(range(row * col + 10))

        def get_ids(r, c):
            return (r - 1) * col + c - 1 + 2  # 0， 1 为 super点

        def find(i):
            ic = i
            while headers[i] != i:
                i = headers[i]
            while ic != i:
                ic, headers[ic] = headers[ic], i
            return i

        def union(a, b):
            a1, b1 = find(a), find(b)
            if a1 != b1:
                if b1 == 0 or b1 == 1:
                    a1, b1 = b1, a1
                headers[b1] = a1

        # moves = [0, 1, 0, -1, 0]
        # lands = set()
        # for i in range(len(cells) - 1, -1, -1):
        #     a, b = cells[i]
        #     lands.add((a, b))
        #     for _ in range(4):
        #         na, nb = a + moves[_], b + moves[_ + 1]
        #         if 1 <= na <= row and 1 <= nb <= col and (na, nb) in lands:
        #             union(get_ids(a, b), get_ids(na, nb))
        #     if a == 1:
        #         union(get_ids(a, b), 0)
        #     if a == row:
        #         union(get_ids(a, b), 1)
        #
        #     if find(0) == find(1):
        #         return i
        waters = set()
        for i in range(len(cells)):
            a, b = cells[i]
            waters.add((a, b))
            for i1, i2 in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                na, nb = a + i1, b + i2
                if 1 <= na <= row and 1 <= nb <= col and (na, nb) in waters:
                    union(get_ids(a, b), get_ids(na, nb))
            if b == 1:
                union(get_ids(a, b), 0)
            if b == col:
                union(get_ids(a, b), 1)
            if find(0) == find(1):
                return i

        return -1
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().latestDayToCross(row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]))
    print(Solution().latestDayToCross(row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]))
    print(Solution().latestDayToCross(row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3 ,2],[3,1]]))