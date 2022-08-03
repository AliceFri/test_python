from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s = sorted(heights)

        iRet = 0
        for i in range(len(heights)):
            if s[i] != heights[i]:
                iRet += 1

        return iRet
