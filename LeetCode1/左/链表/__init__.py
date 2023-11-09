"""
0. 反转链表                 递归/迭代
1. 找到链表中间的结点        快慢指针
2. 判断链表是否回文         快慢指针找到中点， 后面的node压到栈里，一个个弹出与开头开始比较 | 找到中点后 （倒序后续链表，比较两条链表）
3. 链表 Partition         3个dummy头 （<, = , >）
4. 带rand指针的单链表的复制   哈希表 | 把复制结点先放到旧结点的next位置 1 -> 1' -> 2 -> 2' -> 3 -> 3' -> null

5. 两个链表的相交的第一个结点或不相交    双指针
6. 判断一个链表是否成环               快慢指针

7. 不告诉头结点，给删除的结点能做到吗        不行
"""


class Node:
    def __init__(self, val=0, nex=None, pre=None):
        self.val = val
        self.next = nex
        self.pre = pre

    def __str__(self):
        return f"{self.val} -> {self.next}"


def CreateList(arr):
    if not arr:
        return None
    a = [Node(i) for i in arr]

    for i in range(len(a) - 1):
        a[i].next = a[i + 1]
    return a[0]


def CreateTList(arr):
    if not arr:
        return None
    a = [Node(i) for i in arr]

    for i in range(len(a) - 1):
        a[i].next = a[i + 1]
        a[i + 1].pre = a[i]
    return a[0]


if __name__ == "__main__":
    print(CreateList([1, 2, 3, 4, 54]))
