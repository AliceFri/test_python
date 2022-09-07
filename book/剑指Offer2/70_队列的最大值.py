import collections


class MaxQueue:
    def __init__(self):
        self.queue = collections.deque()
        self._max = collections.deque()  # 最后一位存最大值

    def max_value(self) -> int:
        if not self._max:
            return -1
        return self._max[-1]

    def push_back(self, value: int) -> None:
        self.queue.appendleft(value)
        self._max.appendleft(value)
        i = 1
        while i < len(self._max) and value >= self._max[i]:
            self._max[i] = value
            i += 1

    def pop_front(self) -> int:
        if not self._max:
            return -1
        q = self.queue.pop()
        self._max.pop()
        return q


if __name__ == '__main__':
    obj = MaxQueue()
    param_1 = obj.max_value()
    obj.push_back(12)
    obj.push_back(1)
    param_3 = obj.pop_front()
    obj.push_back(2)
    obj.push_back(1)
    param_3 = obj.pop_front()


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
