"""
Hard

如何得到一个数据流中的中位数。
"""

import heapq


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # 一个最小堆， 一个最大堆。 维持两个堆size相等
        self._min = []
        self._max = []  # python 默认为最小堆， 最大堆放入和取出的时候需要取反

    def addNum(self, num: int) -> None:
        if not self._min or num >= self._min[0]:
            heapq.heappush(self._min, num)
        else:
            heapq.heappush(self._max, -num)

        while len(self._max) > len(self._min):
            a = -heapq.heappop(self._max)
            heapq.heappush(self._min, a)

        while len(self._min) > len(self._max) + 1:
            a = heapq.heappop(self._min)
            heapq.heappush(self._max, -a)

    def findMedian(self) -> float:
        if not self._max and not self._min:
            return -1
        if len(self._max) == len(self._min):
            return (-self._max[0] + self._min[0]) / 2
        return self._min[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(-1)
    obj.addNum(-2)
    obj.addNum(-3)
    obj.addNum(-4)
    obj.addNum(-5)