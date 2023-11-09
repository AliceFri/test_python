"""
Easy

1. 排序 取前k个数
2. size为k的最大堆 n log k时间复杂度
3. 快排思想
"""
import heapq
from typing import List
import random


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:

        # 堆
        # return heapq.nsmallest(k, arr)

        # 快排思想
        def _partion(a, b):
            if a == b:
                return a
            i = random.randint(a + 1, b)
            arr[i], arr[a] = arr[a], arr[i]
            iflag = arr[a]              # 更简单的是从右边选定标准值
            icmp, iswp = a, a
            for i in range(a + 1, b + 1):
                if arr[i] <= iflag:
                    arr[i], arr[icmp] = arr[icmp], arr[i]
                    if iswp == i:
                        iswp = icmp
                    elif iswp == icmp:
                        iswp = i
                    icmp += 1
            arr[iswp] = arr[icmp]
            arr[icmp] = iflag
            return icmp

        def _find(a, b):
            _k = _partion(a, b)
            if _k == k - 1:
                a = arr[0: k]
                a.sort()
                return a
            if _k < k - 1:
                return _find(_k + 1, b)
            return _find(a, _k - 1)

        return _find(0, len(arr) - 1)


if __name__ == '__main__':
    print([0,0,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,4,5,5,5,6,6,6,7,7,7,7,7,8,8,8,8,9,9,10,10,10,10,11,12,12,12,13,15,15,16,17,17,18,19,19,19,19,20,22,22,22,22,23,26,26,27,27,28,29,31,32,33,35,36,39,40,42])
    print(Solution().getLeastNumbers([0,1,1,1,4,5,3,7,7,8,10,2,7,8,0,5,2,16,12,1,19,15,5,18,2,2,22,15,8,22,17,6,22,6,22,26,32,8,10,11,2,26,9,12,9,7,28,33,20,7,2,17,44,3,52,27,2,23,19,56,56,58,36,31,1,19,19,6,65,49,27,63,29,1,69,47,56,61,40,43,10,71,60,66,42,44,10,12,83,69,73,2,65,93,92,47,35,39,13,75],75))

