# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode
from typing import Optional


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        sum = 0
        if not root:
            return 0

        def trans(r, l):
            nonlocal sum
            l.append(str(r.val))
            if not r.left and not r.right:
                i = "".join(l)
                sum += int(i, base=2)
            else:
                if r.left:
                    trans(r.left, l[:])
                if r.right:
                    trans(r.right, l[:])

        trans(root, [])
        return sum