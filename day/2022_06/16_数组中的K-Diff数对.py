from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()

        res = set()

        for a in range(0, len(nums) - 1):
            for b in range(a + 1, len(nums)):

                if (nums[b] - nums[a]) > k:
                    break
                elif (nums[b] - nums[a]) == k:
                    res.add((nums[a], nums[b]))
                    break

        return len(res)