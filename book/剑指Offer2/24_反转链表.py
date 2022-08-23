"""
Easy

反转链表
"""
from book.剑指Offer2 import ListNode, l1


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 递归做法
        if not head or not head.next:
            return head

        n = head.next
        head.next = None
        p = self.reverseList(n)
        n.next = head
        return p


if __name__ == '__main__':
    print(Solution().reverseList(l1))
