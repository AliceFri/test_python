# arr = [1,2,3,4,5], k = 4, x = 3
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr1 = [abs(i - x) for i in arr]
        pre = [0]
        imin = 10**5
        imind = 0
        for i in range(len(arr1)):
            pre.append(pre[-1] + arr1[i])
            if i >= k - 1:
                if pre[i + 1] - pre[i + 1 - k] < imin:
                    imin = pre[i + 1] - pre[i + 1 - k]
                    imind = i
        return arr[imind - k + 1 : imind + 1]


if __name__ == '__main__':
    print(Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3))
