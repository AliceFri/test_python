import random
from typing import List


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.arer = []
        self.area_sum = 0
        self.rects = rects
        for a1, a2, b1, b2 in rects:
            iArea = (b2 - a2 + 1) * (b1 - a1 + 1)
            self.arer.append(iArea)
            self.area_sum += iArea

    def pick(self) -> List[int]:
        # print(self.area_sum)
        iRand1 = random.randint(1, self.area_sum)
        iTmp = 0
        iChoose = 0
        # print(self.arer, iRand1)
        for ind, i in enumerate(self.arer):
            iTmp += i
            if iRand1 <= iTmp:
                iChoose = ind
                break
        # print(iChoose)

        # print(self.rects[iChoose], iChoose)
        a1, a2 = self.rects[iChoose][0], self.rects[iChoose][1]
        b1, b2 = self.rects[iChoose][2], self.rects[iChoose][3]
        return [random.randint(a1, b1), random.randint(a2, b2)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

# 前缀和 + 二分查找
# 水塘抽样 节省空间