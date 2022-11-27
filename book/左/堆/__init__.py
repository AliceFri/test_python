import heapq
from typing import List

"""
堆结构

完全二叉树 size
i -> i * 2 + 1, i * 2 + 2       # 找子结点
i -> (i - 1) // 2               # 找父结点
"""


# 堆排序
def heap_sort(arr: List) -> List:
    h = Heap(arr)
    # for i in arr:
    #     h.heappush(i)
    res = []
    for i in arr:
        res.append(h.heappop())
    return res


# 大根堆
class Heap:
    def __init__(self, arr=None):
        if not arr:
            self.nums = []
        else:
            self.nums = arr[::]
            self.heapify()

    def heappush(self, i):
        self.nums.append(i)
        ind = len(self.nums) - 1
        self.shiftdown(ind)

    def heapify(self):
        """
        O(n) 时间复杂度， 建成堆
        """
        for i in range(len(self.nums) - 1, -1, -1):
            self.shiftdown(i)

    def shiftdown(self, ind):
        while ind > 0 and self.nums[ind] > self.nums[((ind - 1) >> 1)]:
            self.nums[ind], self.nums[((ind - 1) >> 1)] = (
                self.nums[((ind - 1) >> 1)],
                self.nums[ind],
            )
            ind = (ind - 1) >> 1

    def shiftup(self, ind):
        left, right = 2 * ind + 1, 2 * ind + 2
        ichange = -1
        if left > len(self.nums) - 1:
            return
        # 先比较左孩子
        if self.nums[left] > self.nums[ind]:
            ichange = left
        # 再比较右孩子
        if right <= len(self.nums) - 1 and self.nums[right] > self.nums[left]:
            ichange = right
        if ichange != -1:
            self.nums[ichange], self.nums[ind] = self.nums[ind], self.nums[ichange]
            self.shiftup(ichange)

    def heappop(self):
        if not self.nums:
            return
        res = self.nums[0]
        self.nums[0] = self.nums[-1]
        self.nums.pop(-1)
        self.shiftup(0)
        return res

    def info(self):
        print(self.nums)


if __name__ == "__main__":
    # h = Heap()
    # for i in range(10):
    #     h.heappush(i)
    # h.info()
    # for i in range(10):
    #     print(h.heappop())
    # h.info()
    # 堆排序
    print(heap_sort([1, 10, 2, 3, 4, 3, 9, 2]))
    # heapify
    h = Heap(arr=[i for i in range(10)])
    h.info()
