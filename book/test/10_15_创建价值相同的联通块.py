from typing import List

# nums = [6,2,2,2,6], edges = [[0,1],[1,2],[1,3],[3,4]]


class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:

        n = len(nums)

        # 建图
        e = [[] for _ in range(n)]
        for edge in edges:
            e[edge[0]].append(edge[1])
            e[edge[1]].append(edge[0])

        # 计算每个子树的权值之和
        f = [0] * n

        def dfs1(sn, fa):
            f[sn] = nums[sn]
            for fn in e[sn]:
                if fn != fa:
                    dfs1(fn, sn)
                    f[sn] += f[fn]

        dfs1(0, -1)
        print(f)


if __name__ == "__main__":
    Solution().componentValue(
        nums=[6, 2, 2, 2, 6], edges=[[0, 1], [1, 2], [1, 3], [3, 4]]
    )
