# 给定一个链表的 头节点 head ，请判断其是否为回文链表。 
# 
#  如果一个链表是回文，那么链表节点序列从前往后看和从后往前看是相同的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入: head = [1,2,3,3,2,1]
# 输出: true 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入: head = [1,2]
# 输出: false
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表 L 的长度范围为 [1, 10⁵] 
#  0 <= node.val <= 9 
#  
# 
#  
# 
#  进阶：能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
# 
#  
# 
#  注意：本题与主站 234 题相同：https://leetcode-cn.com/problems/palindrome-linked-list/ 
#  Related Topics 栈 递归 链表 双指针 👍 54 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#     def __str__(self):
#         return f"{self.val} -> {self.next}"

class Solution:
    def reverse(self, head):
        if not head or not head.next:
            return head
        p_next = head.next
        head.next = None
        while p_next:
            p_tmp = p_next.next
            p_next.next = head
            head = p_next
            p_next = p_tmp
        return head

    def isPalindrome(self, head: ListNode) -> bool:

        if not head or not head.next:
            return True

        # 快慢指针找到中点
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        half = slow.next
        half = self.reverse(half)

        while half:
            if half.val != head.val:
                return False
            half = half.next
            head = head.next
        return True
# leetcode submit region end(Prohibit modification and deletion)
