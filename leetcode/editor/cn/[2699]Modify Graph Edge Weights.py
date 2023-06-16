# You are given an undirected weighted connected graph containing n nodes 
# labeled from 0 to n - 1, and an integer array edges where edges[i] = [ai, bi, wi] 
# indicates that there is an edge between nodes ai and bi with weight wi. 
# 
#  Some edges have a weight of -1 (wi = -1), while others have a positive 
# weight (wi > 0). 
# 
#  Your task is to modify all edges with a weight of -1 by assigning them 
# positive integer values in the range [1, 2 * 10⁹] so that the shortest distance 
# between the nodes source and destination becomes equal to an integer target. If there 
# are multiple modifications that make the shortest distance between source and 
# destination equal to target, any of them will be considered correct. 
# 
#  Return an array containing all edges (even unmodified ones) in any order if 
# it is possible to make the shortest distance from source to destination equal to 
# target, or an empty array if it's impossible. 
# 
#  Note: You are not allowed to modify the weights of edges with initial 
# positive weights. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, 
# destination = 1, target = 5
# Output: [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
# Explanation: The graph above shows a possible modification to the edges, 
# making the distance from 0 to 1 equal to 5.
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target 
# = 6
# Output: []
# Explanation: The graph above contains the initial edges. It is not possible 
# to make the distance from 0 to 2 equal to 6 by modifying the edge with weight -1. 
# So, an empty array is returned.
#  
# 
#  Example 3: 
# 
#  
# 
#  
# Input: n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, 
# destination = 2, target = 6
# Output: [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
# Explanation: The graph above shows a modified graph having the shortest 
# distance from 0 to 2 as 6.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 100 
#  1 <= edges.length <= n * (n - 1) / 2 
#  edges[i].length == 3 
#  0 <= ai, bi < n 
#  wi = -1 or 1 <= wi <= 107 
#  ai != bi 
#  0 <= source, destination < n 
#  source != destination 
#  1 <= target <= 10⁹ 
#  The graph is connected, and there are no self-loops or repeated edges 
#  
#  Related Topics 图 最短路 堆（优先队列） 👍 62 👎 0
import heapq
from collections import defaultdict
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        # 1. 建 图
        p = defaultdict(list)
        for a, b, c in edges:
            p[a].append((b, c))
            p[b].append((a, c))
        # 判断 有没有更短的路
        des1 = {source: 0}  # des1 代表不能经过 -1
        heap = []
        for l in p[source]:
            heapq.heappush(heap, (l[1], source, l[0]))
        while heap:
            d, f, t = heapq.heappop(heap)
            if d == -1:
                continue
            bneedadd = t not in des1
            _d = des1[f]
            if t not in des1:
                des1[t] = _d + d
            else:
                des1[t] = min(des1[t], _d + d)

            if bneedadd:
                for l in p[t]:
                    if l[0] not in des1:
                        heapq.heappush(heap, (l[1], t, l[0]))
        if destination in des1 and des1[destination] < target:
            return []


        # 2. 初始化
        des = {source: (0, [], 0)}

        heap = []
        for l in p[source]:
            heapq.heappush(heap, (l[1], source, l[0]))

        def set_des(t, aim):
            if t not in des:
                des[t] = aim
            else:
                if aim[0] + len(aim[1]) < des[t][0] + len(des[t][1]):
                    des[t] = (aim[0], aim[1], min(aim[2], des[t][2]))
                else:
                    des[t] = (des[t][0], des[t][1], min(aim[2], des[t][2]))

        while heap:
            d, f, t = heapq.heappop(heap)
            bneedadd = t not in des
            _d, _l, _less = des[f]
            _l = _l[:]
            if d == -1:
                _l.append((f, t))
                set_des(t, (_d, _l, _less))
            else:
                set_des(t, (_d + d, _l, _less + d))

            if bneedadd:
                for l in p[t]:
                    if l[0] not in des:
                        heapq.heappush(heap, (l[1], t, l[0]))

        if destination not in des or (des[destination][0] + len(des[destination][1])) > target or (des[destination][0] < target and len(des[destination][1]) <= 0):
            return []

        all_one = False
        a, b, c = 0, 0, 0
        if len(des[destination][1]) + des[destination][0] == target:
            all_one = True
        else:
            a, b = des[destination][1][0]
            c = target - des[destination][0] - len(des[destination][1]) + 1

        ans = []
        for l in edges:
            if l[2] != -1:
                ans.append((l[0], l[1], l[2]))
            else:
                if (not all_one) and ((l[0] == a and l[1] == b) or (l[0] == b and l[1] == a)):
                    ans.append((l[0], l[1], c))
                else:
                    ans.append((l[0], l[1], 1))
        return ans


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # print(Solution().modifiedGraphEdges(5, [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], 0, 1, 5))
    # print(Solution().modifiedGraphEdges(3, [[0,1,-1],[0,2,5]], 0, 2, 6))
    # print(Solution().modifiedGraphEdges(4, [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], 0, 2, 6))

    print(Solution().modifiedGraphEdges(5, [[1,4,1],[2,4,-1],[3,0,2],[0,4,-1],[1,3,10],[1,0,10]], 0, 2, 15))