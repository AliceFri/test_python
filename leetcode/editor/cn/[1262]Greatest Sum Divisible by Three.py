# Given an integer array nums, return the maximum possible sum of elements of 
# the array such that it is divisible by three. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,6,5,1,8]
# Output: 18
# Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum 
# divisible by 3). 
# 
#  Example 2: 
# 
#  
# Input: nums = [4]
# Output: 0
# Explanation: Since 4 is not divisible by 3, do not pick any number.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,2,3,4,4]
# Output: 12
# Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum 
# divisible by 3).
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 4 * 10⁴ 
#  1 <= nums[i] <= 10⁴ 
#  
#  Related Topics 贪心 数组 动态规划 排序 👍 253 👎 0
from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        l = [[], [], []]
        for i in nums:
            l[i % 3].append(i)
        for ll in l:
            ll.sort(key=lambda x: -x)

        a, b = len(l[1]), len(l[2])
        @cache
        def dfs(a1, b1):
            if a - a1 < 3 and b - b1 < 3 and (a1 >= a or b1 >= a):  # 没有可以加的了
                return 0
            t = 0
            if a - a1 >= 3:
                t = max(t, l[1][a1] + l[1][a1 + 1] + l[1][a1 + 2] + dfs(a1 + 3, b1))
            if b - b1 >= 3:
                t = max(t, l[2][b1] + l[2][b1 + 1] + l[2][b1 + 2] + dfs(a1, b1 + 3))
            if a1 < a and b1 < b:
                t = max(t, l[1][a1] + l[2][b1] + dfs(a1 + 1, b1 + 1))
            return t

        return sum(l[0]) + dfs(0, 0)

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        f = [0, -float("inf"), -float("inf")]
        for num in nums:
            g = f[:]
            for i in range(3):
                g[(i + num % 3) % 3] = max(g[(i + num % 3) % 3], f[i] + num)
            f = g
        return f[0]
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().maxSumDivThree([2,6,2,2,7]))
    # print(Solution().maxSumDivThree([1,2,3,4,4]))
