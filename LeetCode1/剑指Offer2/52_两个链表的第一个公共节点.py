"""
Easy

输入两个链表，找出它们的第一个公共节点。
"""
from LeetCode1.剑指Offer2 import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        p1, p2 = headA, headB
        changea, changeb = False, False
        pa, pb = p1, p2
        while pa and pb:
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next
            if not pa:
                if changea:
                    return None
                changea = True
                pa = p2
            if not pb:
                if changeb:
                    return None
                changeb = True
                pb = p1

        return None