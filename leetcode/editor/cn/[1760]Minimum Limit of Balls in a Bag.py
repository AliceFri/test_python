# You are given an integer array nums where the iᵗʰ bag contains nums[i] balls. 
# You are also given an integer maxOperations. 
# 
#  You can perform the following operation at most maxOperations times: 
# 
#  
#  Take any bag of balls and divide it into two new bags with a positive number 
# of balls.
# 
#  
#  For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or 
# two new bags of 2 and 3 balls. 
#  
#  
#  
# 
#  Your penalty is the maximum number of balls in a bag. You want to minimize 
# your penalty after the operations. 
# 
#  Return the minimum possible penalty after performing the operations. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [9], maxOperations = 2
# Output: 3
# Explanation: 
# - Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
# - Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3]
# .
# The bag with the most number of balls has 3 balls, so your penalty is 3 and 
# you should return 3.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,4,8,2], maxOperations = 4
# Output: 2
# Explanation:
# - Divide the bag with 8 balls into two bags of sizes 4 and 4. [2,4,8,2] -> [2,
# 4,4,4,2].
# - Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,4,4,4,2] -> [
# 2,2,2,4,4,2].
# - Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,4,4,2] ->
#  [2,2,2,2,2,4,2].
# - Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,2,2,4,2] 
# -> [2,2,2,2,2,2,2,2].
# The bag with the most number of balls has 2 balls, so your penalty is 2, and 
# you should return 2.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  1 <= maxOperations, nums[i] <= 10⁹ 
#  
#  Related Topics 数组 二分查找 👍 129 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check_operations(i):
            icnt = 0
            for a in nums:
                icnt += ((a + (i - 1)) // i) - 1
            return icnt <= maxOperations

        il, ir = 1, max(nums)
        ans = 10 ** 9
        while il <= ir:
            im = il + ((ir - il) >> 1)
            if check_operations(im):
                ans = im
                ir = im - 1
            else:
                il = im + 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
