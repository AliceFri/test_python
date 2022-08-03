# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode
from typing import Optional

# 用了层序遍历
# 也可以用广度遍历， mei
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ret = [root]
        i = root.val

        while ret:
            r1 = []
            for r in ret:
                if r.left:
                    r1.append(r.left)
                if r.right:
                    r1.append(r.right)

            ret = r1
            if ret:
                i = ret[0].val

        return i


