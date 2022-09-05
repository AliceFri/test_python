"""
Easy


"""
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        zero_count = 0
        nums.sort()
        imin = imax = None
        for i in nums:
            if i == 0:
                zero_count += 1
            else:
                imin = i
                imax = nums[-1]
                break
        if imax is None:
            return True
        if imax - imin >= 5:
            return False

        if imin > 9:
            imin = 9

        for i in range(imin, imin + 5):
            if i not in nums:
                zero_count -= 1
                if zero_count < 0:
                    return False

        return True

if __name__ == '__main__':
    print(Solution().isStraight([1, 2, 3, 4, 5]))
