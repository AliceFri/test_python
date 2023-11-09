# You are given an integer array nums and an integer threshold. 
# 
#  Find any subarray of nums of length k such that every element in the 
# subarray is greater than threshold / k. 
# 
#  Return the size of any such subarray. If there is no such subarray, return -1
# . 
# 
#  A subarray is a contiguous non-empty sequence of elements within an array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,4,3,1], threshold = 6
# Output: 3
# Explanation: The subarray [3,4,3] has a size of 3, and every element is 
# greater than 6 / 3 = 2.
# Note that this is the only valid subarray.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [6,5,6,5,8], threshold = 7
# Output: 1
# Explanation: The subarray [8] has a size of 1, and 8 > 7 / 1 = 7. So 1 is 
# returned.
# Note that the subarray [6,5] has a size of 2, and every element is greater 
# than 7 / 2 = 3.5. 
# Similarly, the subarrays [6,5,6], [6,5,6,5], [6,5,6,5,8] also satisfy the 
# given conditions.
# Therefore, 2, 3, 4, or 5 may also be returned. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i], threshold <= 10⁹ 
#  
#  Related Topics 栈 并查集 数组 单调栈 👍 28 👎 0
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        # 单调栈, 每个数作为最小值, 的最大长度
        dp = [0] * len(nums)
        dp1 = [0] * len(nums)
        stack = deque()
        for i in range(len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                dp[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        for i in stack:
            dp[i] = len(nums) - i

        stack = deque()
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] < nums[stack[-1]]:
                dp1[stack[-1]] = stack[-1] - i
                stack.pop()
            stack.append(i)
        for i in stack:
            dp1[i] = i + 1

        # print(dp)
        # print(dp1)
        for i in range(len(nums)):
            if nums[i] == 1:
                if dp[i] > threshold:
                    return dp[i]
            elif nums[i] * (dp[i] + dp1[i] - 1) > threshold:
                return dp[i] + dp1[i] - 1
        return -1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().validSubarraySize([1, 3, 4, 3, 1], 6))
