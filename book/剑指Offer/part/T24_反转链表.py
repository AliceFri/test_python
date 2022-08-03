# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。


def reverseList(head):
    if not head or not head.next:
        return head

    next = head.next
    pNext = reverseList(next)
    next.next = head
    head.next = None
    return pNext