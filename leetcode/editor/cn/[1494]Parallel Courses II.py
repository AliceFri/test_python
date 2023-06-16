# You are given an integer n, which indicates that there are n courses labeled 
# from 1 to n. You are also given an array relations where relations[i] = [
# prevCoursei, nextCoursei], representing a prerequisite relationship between course 
# prevCoursei and course nextCoursei: course prevCoursei has to be taken before course 
# nextCoursei. Also, you are given the integer k. 
# 
#  In one semester, you can take at most k courses as long as you have taken 
# all the prerequisites in the previous semesters for the courses you are taking. 
# 
#  Return the minimum number of semesters needed to take all courses. The 
# testcases will be generated such that it is possible to take every course. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 4, relations = [[2,1],[3,1],[1,4]], k = 2
# Output: 3
# Explanation: The figure above represents the given graph.
# In the first semester, you can take courses 2 and 3.
# In the second semester, you can take course 1.
# In the third semester, you can take course 4.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2
# Output: 4
# Explanation: The figure above represents the given graph.
# In the first semester, you can only take courses 2 and 3 since you cannot 
# take more than two per semester.
# In the second semester, you can take course 4.
# In the third semester, you can take course 1.
# In the fourth semester, you can take course 5.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 15 
#  1 <= k <= n 
#  0 <= relations.length <= n * (n-1) / 2 
#  relations[i].length == 2 
#  1 <= prevCoursei, nextCoursei <= n 
#  prevCoursei != nextCoursei 
#  All the pairs [prevCoursei, nextCoursei] are unique. 
#  The given graph is a directed acyclic graph. 
#  
#  Related Topics 位运算 图 动态规划 状态压缩 👍 140 👎 0
from collections import defaultdict
from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        # 课程关系, 每个课程的前列课程
        r = defaultdict(int)
        for pre, nex in relations:
            r[nex] = r[nex] | (1 << (pre - 1))

        iaim = 0
        for i in range(n):
            iaim += (1 << i)

        @cache
        def dfs(itag):
            if itag == iaim:
                return 0
            # 1. 找出 当前 可学的课程
            c = []
            for ii in range(n):
                if (itag & (1 << ii)) == 0 and (itag & r[ii + 1]) == r[ii + 1]:
                    c.append(ii)

            if not c:   # 当前没有可学课程， 学不完所有课程， 题目确保了不会存在
                return -10000

            if len(c) <= k:     # 一次可以学完可学课程
                for a in c:
                    itag += (1 << a)
                return 1 + dfs(itag)

            # 一次学不完  比较麻烦 需要全排列
            ans = 10000

            l = []
            ll = []

            def dfs1(i1):
                if i1 == len(c):
                    if len(l) == k:
                        ll.append(l[:])
                else:
                    l.append(c[i1])
                    dfs1(i1 + 1)
                    l.pop()
                    dfs1(i1 + 1)

            dfs1(0)
            for l in ll:
                itag1 = itag
                for a in l:
                    itag1 += (1 << a)
                ans = min(ans, 1 + dfs(itag1))

            return ans

        return dfs(0)

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().minNumberOfSemesters(4,  [[2,1],[3,1],[1,4]], 2))
    print(Solution().minNumberOfSemesters(5,  [[2,1],[3,1],[4,1],[1,5]], 2))