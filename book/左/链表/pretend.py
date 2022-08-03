from book.左.链表 import *

"""
单链表实现栈
"""


class ListStack:

    def __init__(self):
        self.length = 0
        self.head = Node()

    def add(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        self.length += 1

    def pop(self):
        if not self.length:
            raise Exception('is empty')
        self.length -= 1
        ret = self.head
        self.head = self.head.next
        return ret.val


class ListQueue:

    def __init__(self):
        self.length = 0
        self.head = Node()
        self.tail = self.head

    def add(self, val):
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.length += 1

    def pop(self):
        if not self.length:
            raise Exception('is empty')
        self.length -= 1

        ret = self.head.next
        self.head.next = ret.next
        if not self.length:
            self.head = self.head

        return ret.val

