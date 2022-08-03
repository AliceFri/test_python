from typing import List
import bisect
import math

print(math.gcd(3, 15))


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        dStarts = {}
        for ind in range(len(intervals)):
            dStarts[intervals[ind][0]] = ind

        lStarts = list(dStarts.keys())
        lStarts.sort()

        lRes = []
        for ind in range(len(intervals)):
            y = intervals[ind][1]
            if y > lStarts[-1]:
                lRes.append(-1)
                continue
            i = bisect.bisect_left(lStarts, y)
            lRes.append(dStarts[lStarts[i]])

        return lRes


if __name__ == '__main__':
    print(Solution().findRightInterval([[1, 4], [2, 3], [3, 4]]))
