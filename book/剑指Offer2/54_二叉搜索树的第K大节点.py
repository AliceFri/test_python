"""
Easy

给定一棵二叉搜索树，请找出其中第 k 大的节点的值。
"""
from book.剑指Offer2 import TreeNode


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # 从大往小排 右 -> 根 -> 左
        def _dfs(r):
            nonlocal k
            if r.right:
                res = _dfs(r.right)
                if res:
                    return res
            k -= 1
            if k == 0:
                return r.val
            if r.left:
                res = _dfs(r.left)
                if res:
                    return res

        return _dfs(root)


if __name__ == '__main__':
    print(Solution().kthLargest(TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), 2))