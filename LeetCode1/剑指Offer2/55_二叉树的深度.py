"""
Easy

输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
"""
from LeetCode1.剑指Offer2 import TreeNode, t1


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        i = 0

        def _dfs(r, d):
            nonlocal i
            i = max(i, d)
            if r.right:
                _dfs(r.right, d + 1)
            if r.left:
                _dfs(r.left, d + 1)

        _dfs(root, 1)
        return i


if __name__ == '__main__':
    print(Solution().maxDepth(t1))
