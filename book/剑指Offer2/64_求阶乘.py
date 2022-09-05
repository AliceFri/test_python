"""
Mid

求1 + 2 + ... + n， 要求不使用乘除法，  (n * (n + 1)) // 2
"""


class Solution:
    def sumNums(self, n: int) -> int:
        a, b = n, n + 1
        ans = 0
        while b:
            if b & 1:
                ans += a
            b >>= 1
            a <<= 1
        return ans >> 1


if __name__ == "__main__":
    print(Solution().sumNums(10))
