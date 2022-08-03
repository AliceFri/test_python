# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def cmp_tree(root, val):
            if not root:
                return True
            if root.val != val:
                return False
            return cmp_tree(root.left, val) and cmp_tree(root.right, val)

        if not root:
            return True
        return cmp_tree(root, root.val)