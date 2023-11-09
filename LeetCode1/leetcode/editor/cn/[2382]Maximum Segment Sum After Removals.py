# You are given two 0-indexed integer arrays nums and removeQueries, both of 
# length n. For the iᵗʰ query, the element in nums at the index removeQueries[i] is 
# removed, splitting nums into different segments. 
# 
#  A segment is a contiguous sequence of positive integers in nums. A segment 
# sum is the sum of every element in a segment. 
# 
#  Return an integer array answer, of length n, where answer[i] is the maximum 
# segment sum after applying the iᵗʰ removal. 
# 
#  Note: The same index will not be removed more than once. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1]
# Output: [14,7,2,2,0]
# Explanation: Using 0 to indicate a removed element, the answer is as follows:
# Query 1: Remove the 0th element, nums becomes [0,2,5,6,1] and the maximum 
# segment sum is 14 for segment [2,5,6,1].
# Query 2: Remove the 3rd element, nums becomes [0,2,5,0,1] and the maximum 
# segment sum is 7 for segment [2,5].
# Query 3: Remove the 2nd element, nums becomes [0,2,0,0,1] and the maximum 
# segment sum is 2 for segment [2]. 
# Query 4: Remove the 4th element, nums becomes [0,2,0,0,0] and the maximum 
# segment sum is 2 for segment [2]. 
# Query 5: Remove the 1st element, nums becomes [0,0,0,0,0] and the maximum 
# segment sum is 0, since there are no segments.
# Finally, we return [14,7,2,2,0]. 
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,11,1], removeQueries = [3,2,1,0]
# Output: [16,5,3,0]
# Explanation: Using 0 to indicate a removed element, the answer is as follows:
# Query 1: Remove the 3rd element, nums becomes [3,2,11,0] and the maximum 
# segment sum is 16 for segment [3,2,11].
# Query 2: Remove the 2nd element, nums becomes [3,2,0,0] and the maximum 
# segment sum is 5 for segment [3,2].
# Query 3: Remove the 1st element, nums becomes [3,0,0,0] and the maximum 
# segment sum is 3 for segment [3].
# Query 4: Remove the 0th element, nums becomes [0,0,0,0] and the maximum 
# segment sum is 0, since there are no segments.
# Finally, we return [16,5,3,0].
#  
# 
#  
#  Constraints: 
# 
#  
#  n == nums.length == removeQueries.length 
#  1 <= n <= 10⁵ 
#  1 <= nums[i] <= 10⁹ 
#  0 <= removeQueries[i] < n 
#  All the values of removeQueries are unique. 
#  
#  Related Topics 并查集 数组 有序集合 前缀和 👍 20 👎 0
from typing import List
import bisect

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        # pre = [0] * (len(nums) + 1)
        # for i in range(len(nums)):
        #     pre[i + 1] = pre[i] + nums[i]
        #
        # ans = []
        # ma, mb, mx = 0, 0, None
        # l = [[0, len(nums) - 1]]
        #
        # def get_max(l):
        #     imax = 0
        #     ia, ib = 0, 0
        #     for a, b in l:
        #         if pre[b + 1] - pre[a] > imax:
        #             imax = pre[b + 1] - pre[a]
        #             ia = a
        #             ib = b
        #     return imax, ia, ib
        #
        # for q in removeQueries:
        #     ind = bisect.bisect_right(l, q, key=lambda x: x[0]) - 1
        #     a, b = l[ind]
        #     if a == b == q:
        #         l = l[:ind] + l[ind + 1:]
        #         # l.pop(ind)
        #     elif a == q:
        #         l[ind][0] += 1
        #     elif b == q:
        #         l[ind][1] -= 1
        #     else:
        #         l = l[:ind] + [[a, q - 1], [q + 1, b]] + l[ind + 1:]
        #     if mx is None or (a == ma and b == mb):
        #         mx, ma, mb = get_max(l)
        #     ans.append(mx)
        # return ans
        n = len(nums)
        fa = list(range(n + 1))
        sum = [0] * (n + 1)

        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        ans = [0] * n
        for i in range(n - 1, 0, -1):
            x = removeQueries[i]
            to = find(x + 1)
            fa[x] = to  # 合并 x 和 x+1
            sum[to] += sum[x] + nums[x]
            ans[i - 1] = max(ans[i], sum[to])
        return ans

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().maximumSegmentSum([1,2,5,6,1], [0,3,2,4,1]))
    print(Solution().maximumSegmentSum( [3,2,11,1], [3,2,1,0]))
