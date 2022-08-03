class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # 双指针法

        iLow, iHigh = 0, len(numbers) - 1

        while iLow < iHigh:
            iSum = numbers[iLow] + numbers[iHigh]
            if iSum == target:
                return [iLow, iHigh]
            elif iSum > target:
                iHigh -= 1
            else:
                iLow += 1

        return [-1, -1]