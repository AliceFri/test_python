# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 应用二叉搜索树中序的特性 优化，找到比p大的最小节点
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        match = False
        res = None

        def dfs(root):
            nonlocal match, res
            if root.left:
                dfs(root.left)
            if match and not res:
                res = root
            if root is p:
                match = True
            if root.right:
                dfs(root.right)
        dfs(root)
        return res