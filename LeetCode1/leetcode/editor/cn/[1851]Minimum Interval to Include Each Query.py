# You are given a 2D integer array intervals, where intervals[i] = [lefti, 
# righti] describes the iᵗʰ interval starting at lefti and ending at righti (inclusive)
# . The size of an interval is defined as the number of integers it contains, or 
# more formally righti - lefti + 1. 
# 
#  You are also given an integer array queries. The answer to the jᵗʰ query is 
# the size of the smallest interval i such that lefti <= queries[j] <= righti. If 
# no such interval exists, the answer is -1. 
# 
#  Return an array containing the answers to the queries. 
# 
#  
#  Example 1: 
# 
#  
# Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
# Output: [3,3,1,4]
# Explanation: The queries are processed as follows:
# - Query = 2: The interval [2,4] is the smallest interval containing 2. The 
# answer is 4 - 2 + 1 = 3.
# - Query = 3: The interval [2,4] is the smallest interval containing 3. The 
# answer is 4 - 2 + 1 = 3.
# - Query = 4: The interval [4,4] is the smallest interval containing 4. The 
# answer is 4 - 4 + 1 = 1.
# - Query = 5: The interval [3,6] is the smallest interval containing 5. The 
# answer is 6 - 3 + 1 = 4.
#  
# 
#  Example 2: 
# 
#  
# Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
# Output: [2,-1,4,6]
# Explanation: The queries are processed as follows:
# - Query = 2: The interval [2,3] is the smallest interval containing 2. The 
# answer is 3 - 2 + 1 = 2.
# - Query = 19: None of the intervals contain 19. The answer is -1.
# - Query = 5: The interval [2,5] is the smallest interval containing 5. The 
# answer is 5 - 2 + 1 = 4.
# - Query = 22: The interval [20,25] is the smallest interval containing 22. 
# The answer is 25 - 20 + 1 = 6.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= intervals.length <= 10⁵ 
#  1 <= queries.length <= 10⁵ 
#  intervals[i].length == 2 
#  1 <= lefti <= righti <= 10⁷ 
#  1 <= queries[j] <= 10⁷ 
#  
#  Related Topics 数组 二分查找 排序 扫描线 堆（优先队列） 👍 84 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # 离散化
        l = set()
        for i in intervals:
            l.add(i[0])
            l.add(i[1])
        for i in queries:
            l.add(i)
        l = list(l)
        l.sort()
        n = len(l)
        m = {l[ind]: (ind + 1) for ind in range(n)}
        # 线段树
        lmin = [float('inf')] * (4 * n + 10)
        lazy = [float('inf')] * (4 * n + 10)

        def pushDown(rt):
            if lazy[rt] != float('inf'):
                lazy[rt << 1] = min(lazy[rt], lazy[rt << 1])
                lazy[rt << 1 | 1] = min(lazy[rt], lazy[rt << 1 | 1])
                lmin[rt << 1] = min(lmin[rt << 1], lazy[rt])
                lmin[rt << 1 | 1] = min(lmin[rt << 1 | 1], lazy[rt])
                lazy[rt] = float('inf')

        def pushUp(rt):
            lmin[rt] = min(lmin[rt << 1], lmin[rt << 1 | 1])

        def update(L, R, C, l0, r0, rt):    # 将L - R 的值触发一次更新C， l0, r0, rt为当前处于rt位的值代表l0-r0的范围
            if l0 >= L and r0 <= R:
                # 当前 rt位置被设置范围囊括
                lmin[rt] = min(lmin[rt], C)
                if not lazy[rt]:
                    lazy[rt] = C
                lazy[rt] = min(lazy[rt], C)
                return
            mid = l0 + ((r0 - l0) >> 1)
            pushDown(rt)
            if mid >= L and l0 <= R:
                update(L, R, C, l0, mid, rt << 1)
            if r0 >= L and mid + 1 <= R:
                update(L, R, C, mid + 1, r0, rt << 1 | 1)
            pushUp(rt)

        def query(L, R, l0, r0, rt):
            if l0 >= L and r0 <= R:
                return lmin[rt]
            mid = l0 + ((r0 - l0) >> 1)
            pushDown(rt)
            ans = float('inf')
            if mid >= L and l0 <= R:
                ans = min(ans, query(L, R, l0, mid, rt << 1))
            if r0 >= L and mid + 1 <= R:
                ans = min(ans, query(L, R, mid + 1, r0, rt << 1 | 1))
            pushUp(rt)
            return ans

        # 建树
        for l in intervals:
            update(m[l[0]], m[l[1]], l[1] - l[0] + 1, 1, n, 1)

        ans = []
        for q in queries:
            t = query(m[q], m[q], 1, n, 1)
            if t == float('inf'):
                ans.append(-1)
            else:
                ans.append(t)
        return ans
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().minInterval([[1,4],[2,4],[3,6],[4,4]], [2,3,4,5]))
    print(Solution().minInterval([[1, 4]], [1, 2, 3, 4, 5, 6]))

