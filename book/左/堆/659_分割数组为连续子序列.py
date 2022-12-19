from typing import List

# [1,2,3,3,4,4,5,5]
import heapq


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        h = []
        for i in nums:
            bAdd = False
            while h:
                b, a = h[0]
                if i > b + 1:
                    if a < 3:
                        return False
                    heapq.heappop(h)
                elif i == b + 1:
                    heapq.heappop(h)
                    bAdd = True
                    heapq.heappush(h, (b + 1, a + 1))
                    break
                else:
                    break
            if not bAdd:
                heapq.heappush(h, (i, 1))
        for l in h:
            if l[1] < 3:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isPossible([1, 2, 3, 3, 4, 4, 5, 5]))
