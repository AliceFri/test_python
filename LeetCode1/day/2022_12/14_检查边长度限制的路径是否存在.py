from typing import List

# n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
# 输出：[false,true]

# ：n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
# ：[true,false]
# 2 <= n <= 105
# <= edgeList.length, queries.length <= 105


class Solution:
    def distanceLimitedPathsExist(
        self, n: int, edgeList: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:

        u = [i for i in range(n + 1)]

        def find(i):
            icopy = i
            while i != u[i]:
                i = u[i]
            while icopy != i:
                icopy, u[icopy] = u[icopy], i
            return i

        def union(a, b):
            ia, ib = find(a), find(b)
            u[ia] = ib

        edgeList.sort(key=lambda x: x[2])
        for _, q in enumerate(queries):
            q.append(_)
        queries.sort(key=lambda x: x[2])

        ans = [False] * len(queries)
        ind = 0  # 指向edgeList
        for q in queries:
            a, b, c, d = q
            while ind < len(edgeList) and edgeList[ind][2] < c:
                union(edgeList[ind][0], edgeList[ind][1])
                ind += 1
            if find(a) == find(b):
                ans[d] = True
        return ans


if __name__ == '__main__':
    print(
        Solution().distanceLimitedPathsExist(
            3, [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]], [[0, 1, 2], [0, 2, 5]]
        )
    )
    print(
        Solution().distanceLimitedPathsExist(
            5, [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]], [[0, 4, 14], [1, 4, 13]]
        )
    )
