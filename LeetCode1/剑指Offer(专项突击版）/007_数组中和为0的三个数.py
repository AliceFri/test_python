class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 2:
            return []

        lRet = set()
        nums.sort()

        for a in range(len(nums) - 2):
            iTarget = 0 - nums[a]

            iLow, iHigh = a + 1, len(nums) - 1
            while iLow < iHigh:
                iSum = nums[iLow] + nums[iHigh]
                if iSum == iTarget:
                    lRet.add((nums[a], nums[iLow], nums[iHigh]))
                    iLow += 1
                    iHigh -= 1
                elif iSum > iTarget:
                    iHigh -= 1
                else:
                    iLow += 1

        return list(lRet)