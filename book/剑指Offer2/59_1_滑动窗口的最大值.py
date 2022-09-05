from typing import List
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 有个双向队列， 其最左边位置为当前窗口的最大值， 【_6， _5， _3】 单调栈
        # 动态维护
        stack = collections.deque()
        res = []

        for i in range(0, len(nums)):
            while stack and nums[i] >= nums[stack[-1]]:  # 单调栈的写法
                stack.pop()
            while stack and i - stack[0] >= k:
                stack.popleft()
            stack.append(i)
            if i >= k - 1:
                res.append(nums[stack[0]])

        return res


if __name__ == '__main__':
    print(Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))
