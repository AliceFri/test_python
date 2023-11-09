"""
Easy

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
"""
from LeetCode1.剑指Offer2 import ListNode, l1, l2


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        p = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                p = p.next
                l1 = l1.next
            else:
                p.next = l2
                p = p.next
                l2 = l2.next

        if l1:
            p.next = l1
        elif l2:
            p.next = l2

        return dummy.next


if __name__ == '__main__':
    print(Solution().mergeTwoLists(l1, l2))