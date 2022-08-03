# 前缀和 + 二分查找 nlgn
# 滑动窗口 O(n)


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # 滑动窗口

        iSum = 0  # 滑动窗口的和
        iLeft, iRight = 0, 0  # 窗口为[iLeft, iRight)
        iRet = 100000

        while iRight < len(nums):
            if iSum < target:
                iRight += 1
                iSum += nums[iRight - 1]

            if iSum >= target:
                iRet = min(iRet, iRight - iLeft)
                while iSum >= target:
                    iLeft += 1
                    iSum -= nums[iLeft - 1]

                    if iSum >= target:
                        iRet = min(iRet, iRight - iLeft)

        if iRet == 100000:
            return 0

        return iRet





