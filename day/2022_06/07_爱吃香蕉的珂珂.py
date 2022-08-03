from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def getH(piles, p):
            iSum = 0
            for pi in piles:
                if pi % p == 0:
                    iSum += (pi // p)
                else:
                    iSum += (pi // p)
                    iSum += 1
            return iSum

        piles.sort()

        l, r = 1, piles[-1]

        while l < r:
            m = (r - l) // 2 + l
            h1 = getH(piles, m)
            if h1 > h:
                l = m + 1
            else:
                r = m

        return l
