class Node:

    def __init__(self, val=0, nex=None, pre=None):
        self.val = val
        self.next = nex
        self.pre = pre

    def __str__(self):
        return f'{self.val} -> {self.next}'


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


if __name__ == '__main__':
    print(CreateList([1, 2, 3, 4, 54]))