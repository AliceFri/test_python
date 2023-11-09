# You are given an integer n indicating the number of people in a network. Each 
# person is labeled from 0 to n - 1. 
# 
#  You are also given a 0-indexed 2D integer array restrictions, where 
# restrictions[i] = [xi, yi] means that person xi and person yi cannot become friends, 
# either directly or indirectly through other people. 
# 
#  Initially, no one is friends with each other. You are given a list of friend 
# requests as a 0-indexed 2D integer array requests, where requests[j] = [uj, vj] 
# is a friend request between person uj and person vj. 
# 
#  A friend request is successful if uj and vj can be friends. Each friend 
# request is processed in the given order (i.e., requests[j] occurs before requests[j +
#  1]), and upon a successful request, uj and vj become direct friends for all 
# future friend requests. 
# 
#  Return a boolean array result, where each result[j] is true if the jᵗʰ 
# friend request is successful or false if it is not. 
# 
#  Note: If uj and vj are already direct friends, the request is still 
# successful. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 3, restrictions = [[0,1]], requests = [[0,2],[2,1]]
# Output: [true,false]
# Explanation:
# Request 0: Person 0 and person 2 can be friends, so they become direct 
# friends. 
# Request 1: Person 2 and person 1 cannot be friends since person 0 and person 1
#  would be indirect friends (1--2--0).
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3, restrictions = [[0,1]], requests = [[1,2],[0,2]]
# Output: [true,false]
# Explanation:
# Request 0: Person 1 and person 2 can be friends, so they become direct 
# friends.
# Request 1: Person 0 and person 2 cannot be friends since person 0 and person 1
#  would be indirect friends (0--2--1).
#  
# 
#  Example 3: 
# 
#  
# Input: n = 5, restrictions = [[0,1],[1,2],[2,3]], requests = [[0,4],[1,2],[3,1
# ],[3,4]]
# Output: [true,false,true,false]
# Explanation:
# Request 0: Person 0 and person 4 can be friends, so they become direct 
# friends.
# Request 1: Person 1 and person 2 cannot be friends since they are directly 
# restricted.
# Request 2: Person 3 and person 1 can be friends, so they become direct 
# friends.
# Request 3: Person 3 and person 4 cannot be friends since person 0 and person 1
#  would be indirect friends (0--4--3--1).
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= n <= 1000 
#  0 <= restrictions.length <= 1000 
#  restrictions[i].length == 2 
#  0 <= xi, yi <= n - 1 
#  xi != yi 
#  1 <= requests.length <= 1000 
#  requests[j].length == 2 
#  0 <= uj, vj <= n - 1 
#  uj != vj 
#  
#  Related Topics 并查集 图 👍 31 👎 0
from typing import List
from collections import defaultdict

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        header = list(range(n))
        limit = defaultdict(set)
        for a, b in restrictions:
            limit[a].add(b)
            limit[b].add(a)

        def find(i):
            ic = i
            while i != header[i]:
                i = header[i]
            while ic != i:
                ic, header[ic] = header[ic], i
            return i

        def union(a, b):
            if b in limit[a]:
                return False
            a1, b1 = find(a), find(b)
            if a1 == b1:
                return True
            l1, l2 = [], []
            for i in range(n):
                if find(i) == a1:
                    l1.append(i)
                if find(i) == b1:
                    l2.append(i)
            for i1 in l1:
                for i2 in l2:
                    if i2 in limit[i1]:
                        return False
            header[a1] = b1
            return True

        ans = []
        for a, b in requests:
            ans.append(union(a, b))
        return ans
# leetcode submit region end(Prohibit modification and deletion)
