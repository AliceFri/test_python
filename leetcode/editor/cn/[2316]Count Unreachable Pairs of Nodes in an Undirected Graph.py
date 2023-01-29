# You are given an integer n. There is an undirected graph with n nodes, 
# numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, 
# bi] denotes that there exists an undirected edge connecting nodes ai and bi. 
# 
#  Return the number of pairs of different nodes that are unreachable from each 
# other. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 3, edges = [[0,1],[0,2],[1,2]]
# Output: 0
# Explanation: There are no pairs of nodes that are unreachable from each other.
#  Therefore, we return 0.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
# Output: 14
# Explanation: There are 14 pairs of nodes that are unreachable from each other:
# 
# [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6]
# ,[5,6]].
# Therefore, we return 14.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10⁵ 
#  0 <= edges.length <= 2 * 10⁵ 
#  edges[i].length == 2 
#  0 <= ai, bi < n 
#  ai != bi 
#  There are no repeated edges. 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 图 👍 15 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        s = [1] * n
        header = list(range(n))

        def find(a):
            i = a
            while a != header[a]:
                a = header[a]
            while i != a:
                header[i], i = a, header[i]
            return a

        def union(a, b):
            a1, b1 = find(a), find(b)
            if a1 != b1:
                header[a1] = b1
                s[b1] += s[a1]

        for a, b in edges:
            union(a, b)

        ans = 0
        for i in range(n):
            h = find(i)
            ans += (n - s[h])

        return ans >> 1
# leetcode submit region end(Prohibit modification and deletion)
