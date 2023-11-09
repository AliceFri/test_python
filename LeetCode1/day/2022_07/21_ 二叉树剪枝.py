from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root
        if not root.left and not root.right:
            if root.val == 0:
                return None
            return root

        l1 = self.pruneTree(root.left)
        l2 = self.pruneTree(root.right)
        root.left = l1
        root.right = l2
        if not l1 and not l2 and root.val == 0:
            return None

        return root
