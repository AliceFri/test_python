"""
Mid

请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


"""
1. A -> A' -> B -> B'

2. 借用哈希表
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # import copy
        # return copy.deepcopy(head)
        if not head:
            return head

        p = head
        while p:
            p1 = p.next
            pnew = Node(p.val)
            p.next = pnew
            pnew.next = p1
            p = p1

        p = head
        while p:
            if not p.next:
                break
            if p.random:
                p.next.random = p.random.next
            p = p.next.next

        newhead = head.next
        p = head
        while p and p.next:
            temp = p.next
            p.next = p.next.next
            p = temp

        return newhead
