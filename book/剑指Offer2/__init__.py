"""
35 题 good
43
44
"""


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __str__(self):
        return f'{self.val} -> {self.next}'


l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
l2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def preorder(self):
        # 前序遍历 根 左 右
        r = [self.val]
        if self.left:
            r.extend(self.left.preorder())
        if self.right:
            r.extend(self.right.preorder())
        return r

    def inorder(self):
        # 中序遍历 左根右
        r = []
        if self.left:
            r.extend(self.left.inorder())
        r.append(self.val)
        if self.right:
            r.extend(self.right.inorder())
        return r

    def afterorder(self):
        # 后续遍历 左右根
        r = []
        if self.left:
            r.extend(self.left.afterorder())
        if self.right:
            r.extend(self.right.afterorder())
        r.append(self.val)
        return r


t1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

t2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
t3 = TreeNode(4, TreeNode(1), None)


if __name__ == '__main__':
    print(l1)
    print(t1.preorder())
    print(t1.inorder())
    print(t1.afterorder())
