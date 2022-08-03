class MyCircularQueue:

    def __init__(self, k: int):
        self.lis = [0] * k
        self.begin = 0  # 下次插入的位置
        self.end = 0
        self.size = 0

    def maxsize(self):
        return len(self.lis)

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.size += 1
            self.lis[self.begin] = value
            self.begin = (self.begin + 1) % self.maxsize()
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.end = (self.end + 1) % self.maxsize()
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.lis[self.end]
        # return self.lis[(self.begin - 1) % self.maxsize()]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        # return self.lis[self.end]
        return self.lis[(self.begin - 1) % self.maxsize()]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.lis)

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()