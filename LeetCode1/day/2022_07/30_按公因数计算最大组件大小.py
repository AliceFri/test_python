from collections import Counter
from typing import List


# rank 的作用是为了尽量减少层数！！！！
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        # self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        self.parent[x] = y
        # if self.rank[x] > self.rank[y]:
        #     self.parent[y] = x
        # elif self.rank[x] < self.rank[y]:
        #     self.parent[x] = y
        # else:
        #     self.parent[y] = x
        #     self.rank[x] += 1


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        uf = UnionFind(max(nums) + 1)
        for num in nums:
            i = 2
            while i * i <= num:
                if num % i == 0:
                    uf.merge(num, i)
                    uf.merge(num, num // i)
                i += 1
        return max(Counter(uf.find(num) for num in nums).values())

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/largest-component-size-by-common-factor/solution/an-gong-yin-shu-ji-suan-zui-da-zu-jian-d-amdx/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。