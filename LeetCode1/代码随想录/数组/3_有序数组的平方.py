# 双指针法

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        iLow, iHigh = 0, len(nums) - 1
        rList = [0] * len(nums)
        iTmp = iHigh
        while iLow <= iHigh:
            ia, ib = abs(nums[iLow]), abs(nums[iHigh])
            if ia < ib:
                rList[iTmp] = ib**2
                # rList.insert(0, ib**2)
                iHigh -= 1
            else:
                rList[iTmp] = ia**2
                # rList.insert(0, ia**2)
                iLow += 1
            iTmp -= 1
        return rList