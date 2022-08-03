import random


# 删除，交换要删除的元素和尾部元素的位置，使得O(1)时间内删除
class RandomizedSet:

    def __init__(self):
        self.container = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.container:
            return False
        self.container[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.container:
            return False
        ind = self.container[val]
        val1 = self.list[-1]
        ind2 = self.container[val1]
        self.list[ind], self.list[ind2] = self.list[ind2], self.list[ind]
        self.container[val1] = ind
        del self.container[val]
        self.list.pop(-1)
        return True

    def getRandom(self) -> int:
        return self.list[random.randint(0, len(self.list) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()