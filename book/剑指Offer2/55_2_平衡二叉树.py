"""
Easy

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
"""
from functools import cache

from book.剑指Offer2 import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        @cache
        def _dfs(r):
            if r is None:
                return 0
            return max(_dfs(r.left), _dfs(r.right)) + 1

        l = _dfs(root.left)
        r = _dfs(root.right)
        if abs(l - r) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)