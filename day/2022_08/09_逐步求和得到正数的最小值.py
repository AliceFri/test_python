from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        preSum = [0] * (len(nums) + 1)
        ir = 1
        for i in range(1, len(preSum)):
            preSum[i] = preSum[i - 1] + nums[i - 1]
            it = 1 - preSum[i]

            ir = max(ir, it)

        return ir
