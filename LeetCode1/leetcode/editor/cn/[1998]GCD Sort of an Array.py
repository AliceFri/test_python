# You are given an integer array nums, and you can perform the following 
# operation any number of times on nums: 
# 
#  
#  Swap the positions of two elements nums[i] and nums[j] if gcd(nums[i], nums[
# j]) > 1 where gcd(nums[i], nums[j]) is the greatest common divisor of nums[i] 
# and nums[j]. 
#  
# 
#  Return true if it is possible to sort nums in non-decreasing order using the 
# above swap method, or false otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [7,21,3]
# Output: true
# Explanation: We can sort [7,21,3] by performing the following operations:
# - Swap 7 and 21 because gcd(7,21) = 7. nums = [21,7,3]
# - Swap 21 and 3 because gcd(21,3) = 3. nums = [3,7,21]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [5,2,6,2]
# Output: false
# Explanation: It is impossible to sort the array because 5 cannot be swapped 
# with any other element.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [10,5,9,3,15]
# Output: true
# We can sort [10,5,9,3,15] by performing the following operations:
# - Swap 10 and 15 because gcd(10,15) = 5. nums = [15,5,9,3,10]
# - Swap 15 and 3 because gcd(15,3) = 3. nums = [3,5,9,15,10]
# - Swap 10 and 15 because gcd(10,15) = 5. nums = [3,5,9,10,15]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  2 <= nums[i] <= 10⁵ 
#  
#  Related Topics 并查集 数组 数学 排序 👍 36 👎 0
from typing import List
import math

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        # 每一个连通组的位置 与 排序后的位置保持一致
        l = nums[::]
        l.sort()
        parents = list(range(10 ** 5 + 1))
        sizes = [1] * len(parents)

        def split(n):
            ans = set()
            iflag = 2
            while iflag * iflag <= n:
                while n % iflag == 0:
                    ans.add(iflag)
                    n = n // iflag
                iflag += 1
            if n > 1:
                ans.add(n)
            return ans

        def find(i):
            ic = i
            while i != parents[i]:
                i = parents[i]
            while ic != i:
                ic, parents[ic] = parents[ic], i
            return i

        def union(a, b):
            a1, b1 = find(a), find(b)
            if sizes[b1] < sizes[a1]:
                a1, b1 = b1, a1
            if a1 != b1:
                parents[a1] = b1
                sizes[b1] += sizes[a1]

        for i in nums:
            for a in split(i):
                union(i, a)

        l1 = [find(i) for i in nums]
        l2 = [find(i) for i in l]
        return l1 == l2

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().gcdSort([7,21,3]))
    print(Solution().gcdSort([5, 2, 6, 2]))
    print(Solution().gcdSort([3,5,9,10,15]))
