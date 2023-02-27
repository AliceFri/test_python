# You are given a positive integer n representing the number of nodes in an 
# undirected graph. The nodes are labeled from 1 to n. 
# 
#  You are also given a 2D integer array edges, where edges[i] = [ai, bi] 
# indicates that there is a bidirectional edge between nodes ai and bi. Notice that the 
# given graph may be disconnected. 
# 
#  Divide the nodes of the graph into m groups (1-indexed) such that: 
# 
#  
#  Each node in the graph belongs to exactly one group. 
#  For every pair of nodes in the graph that are connected by an edge [ai, bi], 
# if ai belongs to the group with index x, and bi belongs to the group with index 
# y, then |y - x| = 1. 
#  
# 
#  Return the maximum number of groups (i.e., maximum m) into which you can 
# divide the nodes. Return -1 if it is impossible to group the nodes with the given 
# conditions. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
# Output: 4
# Explanation: As shown in the image we:
# - Add node 5 to the first group.
# - Add node 1 to the second group.
# - Add nodes 2 and 4 to the third group.
# - Add nodes 3 and 6 to the fourth group.
# We can see that every edge is satisfied.
# It can be shown that that if we create a fifth group and move any node from 
# the third or fourth group to it, at least on of the edges will not be satisfied.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3, edges = [[1,2],[2,3],[3,1]]
# Output: -1
# Explanation: If we add node 1 to the first group, node 2 to the second group, 
# and node 3 to the third group to satisfy the first two edges, we can see that 
# the third edge will not be satisfied.
# It can be shown that no grouping is possible.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 500 
#  1 <= edges.length <= 10⁴ 
#  edges[i].length == 2 
#  1 <= ai, bi <= n 
#  ai != bi 
#  There is at most one edge between any pair of vertices. 
#  
#  Related Topics 广度优先搜索 并查集 图 👍 14 👎 0
from typing import List
from collections import defaultdict

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        p = defaultdict(list)
        for a, b in edges:
            p[a].append(b)
            p[b].append(a)

        colors = [0] * (n + 1)

        def dfs(i, icolor):
            # 判断是否二分图
            if colors[i] == icolor:
                return True
            if colors[i] == -icolor:
                return False
            colors[i] = icolor
            for a in p[i]:
                if not dfs(a, -icolor):
                    return False
            return True

        def bfs(i):
            icnt = 0
            vis = set([i])
            q = [i]
            while q:
                _q = []
                for i in q:
                    for a in p[i]:
                        if a not in vis:
                            vis.add(a)
                            _q.append(a)
                icnt += 1
                q = _q
            return icnt

        colorgroup = 1
        for i in range(1, n + 1):
            if colors[i] == 0:
                if not dfs(i, colorgroup):
                    return -1
                colorgroup += 1

        groups = defaultdict(list)
        for i in range(1, len(colors)):
            groups[abs(colors[i])].append(i)

        ans = 0
        for g in groups.values():
            ans += max([bfs(g[i]) for i in range(len(g))])
        return ans
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().magnificentSets(6,
[[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))