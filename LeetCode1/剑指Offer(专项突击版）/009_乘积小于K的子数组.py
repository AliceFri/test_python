class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

# # O(n**2) 超时
# iRet = 0

# for a in range(0, len(nums)):
#     iSum = nums[a]
#     if iSum < k:
#         iRet += 1
#     for b in range(a + 1, len(nums)):
#         iSum *= nums[b]
#         if iSum < k:
#             iRet += 1
#         else:
#             break

# return iRet

        # 用滑动窗口做 O(n)
        pass

