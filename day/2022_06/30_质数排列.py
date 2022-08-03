import bisect
from functools import cache


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        @cache
        def Jie(n):
            if n <= 1:
                return 1
            return n * Jie(n - 1)

        i1 = bisect.bisect_right(prime, n)
        i2 = n - i1
        return Jie(i1) * Jie(i2) % (10 ** 9 + 7)

#         E1  E2  E3  E4  E5  E6
# # Q1    2   3   2   2   3   3       15
# # Q2    1   1   6   1   6   1       16
# # Q3    3   2   3   6   2   6       22
# # Q4    5   6   5   5   5   4       30
# # Q5    4   4   4   4   4   5       25
# # Q6    6   5   1   3   1   2       18
#
# Q1 < Q2 < Q6 < Q3 < Q5 < Q4
