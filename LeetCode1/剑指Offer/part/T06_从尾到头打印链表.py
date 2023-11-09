# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

def reversePrint(self, head) -> list:
    lst = []
    while head:
        lst.insert(0, head.val)
        head = head.next
    return lst