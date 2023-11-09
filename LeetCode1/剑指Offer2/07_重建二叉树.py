"""
Mid

输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
"""
from typing import List

from LeetCode1.剑指Offer2 import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # preorder 根 左 右
        # inorder 左 根 右
        if not preorder:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        r = preorder[0]
        ri = inorder.index(r)
        t = TreeNode(r)
        t.left = self.buildTree(preorder[1 : 1 + ri], inorder[:ri])
        t.right = self.buildTree(preorder[1 + ri :], inorder[ri + 1 :])
        return t


if __name__ == '__main__':
    print(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]).afterorder())
