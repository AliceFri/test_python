from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:

        a1, b1 = points[0]
        a2, b2 = points[1]
        a3, b3 = points[2]

        if a1 == a3 and a2 == a3:
            return False
        if b1 == b2 and b1 == b3:
            return False

        if (b3 - b1) * (a2 - a1) == (b2 - b1) * (a3 - a1):
            return False

        return True