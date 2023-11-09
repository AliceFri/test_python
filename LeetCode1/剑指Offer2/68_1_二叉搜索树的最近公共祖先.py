"""
Easy

所有节点的值都是唯一的。
"""
from LeetCode1.剑指Offer2 import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        if p.val <= root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q)


class Solution1:
    """
    就 二叉树
    """

    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        d = {}

        def _dfs(r):
            if p.val in d and q.val in d:
                return
            if r.left:
                d[r.left.val] = r
                _dfs(r.left)
            if r.right:
                d[r.right.val] = r
                _dfs(r.right)

        _dfs(root)
        # print(d)
        a, b = p.val, q.val
        s1, s2 = set([a]), set([b])
        while True:
            if a not in d and b not in d:
                return None
            if a in d:
                if d[a].val in s2:
                    return d[a]
                s1.add(d[a].val)
                a = d[a].val
            if b in d:
                if d[b].val in s1:
                    return d[b]
                s2.add(d[b].val)
                b = d[b].val
        return None

