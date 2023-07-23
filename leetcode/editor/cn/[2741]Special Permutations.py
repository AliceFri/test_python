# You are given a 0-indexed integer array nums containing n distinct positive 
# integers. A permutation of nums is called special if: 
# 
#  
#  For all indexes 0 <= i < n - 1, either nums[i] % nums[i+1] == 0 or nums[i+1] 
# % nums[i] == 0. 
#  
# 
#  Return the total number of special permutations. As the answer could be 
# large, return it modulo 109 + 7. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,3,6]
# Output: 2
# Explanation: [3,6,2] and [2,6,3] are the two special permutations of nums.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,4,3]
# Output: 2
# Explanation: [3,1,4] and [4,1,3] are the two special permutations of nums.
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= nums.length <= 14 
#  1 <= nums[i] <= 10⁹ 
#  
#  👍 19 👎 0
from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7

        @cache
        def dfs(flag, before):
            if flag.bit_count() == len(nums):
                return 1

            ans = 0
            if flag == 0:  # 代表一个数都没选, 可以选任意数
                for i in range(len(nums)):
                    ans += dfs(1 << i, nums[i])
                    ans = ans % mod
                return ans
            else:
                for i in range(len(nums)):
                    if not (flag & (1 << i)) and (nums[i] % before == 0 or before % nums[i] == 0):
                        ans += dfs(flag | (1 << i), nums[i])
                        ans = ans % mod
            return ans

        return dfs(0, 0)
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().specialPerm([2,3,6]))