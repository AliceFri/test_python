"""
Mid

给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
"""
from typing import List

from LeetCode1.剑指Offer2 import TreeNode, t1


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res = []

        def _pathSum(node, iSum, path):
            if not node:
                return
            it = node.val + iSum
            if not node.left and not node.right and it == target:
                path.append(node.val)
                res.append(path[::])
                path.pop(-1)
            elif node.left:
                path.append(node.val)
                _pathSum(node.left, it, path)
                path.pop(-1)
            elif node.right:
                path.append(node.val)
                _pathSum(node.left, it, path)
                path.pop(-1)

        _pathSum(root, 0, [])

        return res


if __name__ == '__main__':
    print(Solution().pathSum(t1, 12))