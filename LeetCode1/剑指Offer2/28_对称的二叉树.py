"""
Easy

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
"""
from LeetCode1.剑指Offer2 import TreeNode

root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def checkMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            return checkMirror(t1.left, t2.right) and checkMirror(t1.right, t2.left)

        if not root:
            return True
        return checkMirror(root.left, root.right)


if __name__ == '__main__':
    print(Solution().isSymmetric(root))