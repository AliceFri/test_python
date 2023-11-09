from random import randint
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()

        iRet = 0
        iLeft, iRight = 0, len(nums) - 1
        while iLeft < iRight:
            if nums[iLeft] == nums[iRight]:
                break

            iRet += (nums[iRight] - nums[iLeft])
            iLeft += 1
            iRight -= 1

        return iRet


class Helper:
    @staticmethod
    def partition(nums: List[int], l: int, r: int) -> int:
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    @staticmethod
    def randomPartition(nums: List[int], l: int, r: int) -> int:
        i = randint(l, r)
        nums[r], nums[i] = nums[i], nums[r]
        return Helper.partition(nums, l, r)

    @staticmethod
    def quickSelected(nums: List[int], l: int, r: int, k: int) -> int:
        index = Helper.randomPartition(nums, l, r)
        if k == index:
            return nums[k]
        if k < index:
            return Helper.quickSelected(nums, l, index - 1, k)
        return Helper.quickSelected(nums, index + 1, r, k)


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        x = Helper.quickSelected(nums, 0, len(nums) - 1, len(nums) // 2)
        return sum(abs(num - x) for num in nums)


if __name__ == '__main__':
    print(Solution().minMoves2([1, 321, 21, 21, 2, 32, 4, 5, 12, 2]))