# 给定单链表的头节点 head ，请反转链表，并返回反转后的链表的头节点。 
# 
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1,2]
# 输出：[2,1]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目范围是 [0, 5000] 
#  -5000 <= Node.val <= 5000 
#  
# 
#  
# 
#  进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？ 
#  
#  
# 
#  
# 
#  注意：本题与主站 206 题相同： https://leetcode-cn.com/problems/reverse-linked-list/ 
#  Related Topics 递归 链表 👍 62 👎 0


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
    def reverseList(self, head: ListNode) -> ListNode:
        # 迭代法
        # if not head:
        #     return head
        # p_next = head.next
        # head.next = None
        # while p_next:
        #     p_tmp = p_next.next
        #     p_next.next = head
        #     head = p_next
        #     p_next = p_tmp
        #
        # return head

        # 递归法
        if not head or not head.next:
            return head

        p_next = head.next
        head.next = None        # 这一步骤 很容易被忘掉
        p_last = self.reverseList(p_next)
        p_next.next = head
        return p_last


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(ListNode(1, ListNode(2, ListNode(3))))
    print(Solution().reverseList(ListNode(1, ListNode(2, ListNode(3)))))
