"""
Mid

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # 二叉搜索树 的中序遍历 左 根 右 为有序的
        head, pre = None, None

        def dfs(r):
            nonlocal head, pre
            if r.left:
                dfs(r.left)
            if not pre:
                head = r
                pre = r
            else:
                pre.right = r
                r.left = pre
                pre = root
            if r.right:
                dfs(r.right)

        dfs(root)
        if pre:
            pre.right = head
            head.left = pre

        return head