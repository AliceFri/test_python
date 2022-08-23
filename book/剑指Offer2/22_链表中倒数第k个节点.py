"""
Easy

输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。
"""
from book.剑指Offer2 import ListNode, l1


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p1, p2 = head, head
        for i in range(k):
            if not p2:
                return None
            p2 = p2.next

        while p2:
            p2 = p2.next
            p1 = p1.next

        return p1


if __name__ == '__main__':
    print(Solution().getKthFromEnd(l1, 6))