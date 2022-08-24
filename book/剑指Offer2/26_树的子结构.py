"""
Mid

输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict

from book.剑指Offer2 import TreeNode, t1, t3, t2


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        # if not B:
        #     return False
        #
        # def bfs(t):
        #     res = defaultdict(list)
        #
        #     def _bfs(r, h):
        #         if not r:
        #             return
        #         lv = None if not r.left else r.left.val
        #         rv = None if not r.right else r.right.val
        #         hv = None if not h else h.val
        #         res[r.val].append((hv, lv, rv))
        #         if r.left:
        #             _bfs(r.left, r)
        #         if r.right:
        #             _bfs(r.right, r)
        #
        #     _bfs(t, None)
        #     return res
        #
        # def match(t1, t2):
        #     h1, l1, r1 = t1
        #     h2, l2, r2 = t2
        #     if h1 is not None and h1 != h2:
        #         return False
        #     if l1 is not None and l1 != l2:
        #         return False
        #     if r1 is not None and r1 != r2:
        #         return False
        #     return True
        #
        # a = bfs(A)
        # b = bfs(B)
        #
        # for k, v in b.items():
        #     if k not in a:
        #         return False
        #     for _v in v:
        #         bMatch = False
        #         for _v1 in a[k]:
        #             if match(_v, _v1):
        #                 bMatch = True
        #                 break
        #         if not bMatch:
        #             return False
        # return True

        def recur(A, B):
            """
            判断A是否包含B ,且A节点即对应B节点
            """
            if not B:
                return True
            if not A:
                return False
            if A.val != B.val:
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        if not A or not B:
            return False

        if recur(A, B):
            return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)


if __name__ == '__main__':
    print(Solution().isSubStructure(t2, t3))