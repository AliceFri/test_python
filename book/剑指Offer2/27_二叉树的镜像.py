"""
Easy

二叉树的镜像
"""
from book.剑指Offer2 import TreeNode, t1


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        l = None if not root.left else self.mirrorTree(root.left)
        r = None if not root.right else self.mirrorTree(root.right)
        root.left = r
        root.right = l
        return root


if __name__ == '__main__':
    print(Solution().mirrorTree(t1))