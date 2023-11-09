class MyCircularDeque:

    def __init__(self, k: int):
        self.nums = [0] * k
        self.size = 0
        self.maxsize = k
        self.left = 0
        self.right = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.nums[0] = value
            self.left = self.right = 0
        else:
            self.left = (self.left - 1) % self.maxsize
            self.nums[self.left] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.nums[0] = value
            self.left = self.right = 0
        else:
            self.right = (self.right + 1) % self.maxsize
            self.nums[self.right] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.left = (self.left + 1) % self.maxsize
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.right = (self.right - 1) % self.maxsize
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.nums[self.left]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.nums[self.right]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxsize


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()