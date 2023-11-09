from LeetCode1.左.链表 import *


def single_list_reverse(node):
    """
    单链表反转
    :param node:
    :return:
    """

    # 官方迭代
    def gf(node):
        pre, nex = None, None
        while node:
            nex = node.next
            node.next = pre
            pre = node
            node = nex
        return pre

    # return gf(node)

    def dfs(node):
        if not node or not node.next:
            return node
        n1 = node.next
        node.next = None
        p = dfs(n1)
        n1.next = node
        return p

    # node = dfs(node)

    # 迭代法
    p = node.next
    node.next = None
    while p:
        p1 = p.next
        p.next = node
        node = p
        p = p1

    return node


if __name__ == '__main__':
    print(CreateList([1, 2, 3, 4, 5]))
    print(single_list_reverse(CreateList([1, 2, 3, 4, 5])))