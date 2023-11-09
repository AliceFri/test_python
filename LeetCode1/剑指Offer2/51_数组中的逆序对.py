"""
Hard

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
"""
from typing import List


"""
树状数组是一种实现了高效查询「前缀和」与「单点更新」操作的数据结构
"""
from typing import List


# class Solution:
#
#     def reversePairs(self, nums: List[int]) -> int:
#
#         class FenwickTree:
#             def __init__(self, n):
#                 self.size = n
#                 self.tree = [0 for _ in range(n + 1)]
#
#             def __lowbit(self, index):  # 是x的二进制表达式中最低位的1所对应的值
#                 return index & (-index)
#
#             # 单点更新：从下到上，最多到 len，可以取等
#             def update(self, index, delta):
#                 while index <= self.size:
#                     self.tree[index] += delta
#                     index += self.__lowbit(index)
#
#             # 区间查询：从上到下，最少到 1，可以取等
#             def query(self, index):
#                 res = 0
#                 while index > 0:
#                     res += self.tree[index]
#                     index -= self.__lowbit(index)
#                 return res
#
#         # 特判
#         size = len(nums)
#         if size < 2:
#             return 0
#
#         # 原始数组去除重复以后从小到大排序，这一步叫做离散化
#         s = list(set(nums))
#
#         # 构建最小堆，因为从小到大一个一个拿出来，用堆比较合适
#         import heapq
#         heapq.heapify(s)
#
#         # 由数字查排名
#         rank_map = dict()
#         rank = 1
#         # 不重复数字的个数
#         rank_map_size = len(s)
#         for _ in range(rank_map_size):
#             num = heapq.heappop(s)
#             rank_map[num] = rank
#             rank += 1
#
#         res = 0
#         # 树状数组只要不重复数字个数这么多空间就够了
#         ft = FenwickTree(rank_map_size)
#
#         # 从后向前看，拿出一个数字来，就更新一下，然后向前查询比它小的个数
#         for i in range(size - 1, -1, -1):
#             rank = rank_map[nums[i]]
#             ft.update(rank, 1)
#             res += ft.query(rank - 1)
#         return res

class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        class BIT:
            def __init__(self, size):
                self._nums = [0] * (size + 1)       #

            def __lowbit(self, index):
                return index & (-index)

            def update(self, index, iadd):
                while 0 < index <= len(self._nums):
                    self._nums[index] += iadd
                    index += self.__lowbit(index)

            def query(self, index):
                res = 0
                while 0 < index <= len(self._nums):
                    res += self._nums[index]
                    index -= self.__lowbit(index)
                return res

        numset = set(nums)
        n = len(numset)
        lnums = list(numset)
        lnums.sort()
        rankmap = {}
        for i in range(len(lnums)):
            rankmap[lnums[i]] = i

        bitree = BIT(n)

        res = 0
        for i in range(len(nums) - 1, -1, -1):
            r = rankmap[nums[i]] + 1
            bitree.update(r, 1)
            res += bitree.query(r - 1)
        return res


if __name__ == '__main__':
    print(Solution().reversePairs([7, 5, 6, 4]))
