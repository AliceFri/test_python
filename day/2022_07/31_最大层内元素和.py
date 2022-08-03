# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        res = 0
        m = None

        p = [root]
        l = 0

        while p:
            s = sum([v.val for v in p])
            l += 1
            if m is None or s > m:
                m = s
                res = l

            p1 = []
            for r in p:
                if r.left:
                    p1.append(r.left)
                if r.right:
                    p1.append(r.right)
            p = p1

        return res
