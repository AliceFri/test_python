"""
Easy

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
"""
from typing import List

from LeetCode1.剑指Offer2 import ListNode, l1


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l[::-1]


if __name__ == '__main__':
    print(Solution().reversePrint(l1))