from typing import List
import heapq

# [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# ans [20, 24]

"""
有序列表 

[0, 4, 5]   0, 5
[4, 5, 9]   4, 9
[5, 9, 10]  5, 10
[9, 10, 18] 9, 18
[10, 12, 18]    10, 18
[12, 15, 18]    12, 18
[15, 18, 20]    15, 20
[18, 20, 24]    18, 24
[20, 22, 24]    20, 24

"""


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        h = []
        a1, a2, im = 0, 0, 10**5
        # 入堆
        for i in range(len(nums)):
            h.append((nums[i][0], i, 0))
            a2 = max(a2, nums[i][0])

        heapq.heapify(h)
        a1 = h[0][0]
        ans1, ans2 = a1, a2

        while h and h[0][2] < len(nums[h[0][1]]) - 1:
            a, b, c = heapq.heappop(h)
            heapq.heappush(h, (nums[b][c + 1], b, c + 1))
            a1 = h[0][0]
            a2 = max(a2, nums[b][c + 1])
            if a2 - a1 < ans2 - ans1:
                ans1, ans2 = a1, a2
        return [ans1, ans2]


if __name__ == '__main__':
    print(
        Solution().smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
    )
    print(Solution().smallestRange([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
