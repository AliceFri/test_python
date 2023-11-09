"""
Mid

实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        快速mi 迭代法比递归更难，
        1010 x ** 10 == (x ** (2 ** 1)) * (x ** (2 ** 3))
        1和3恰好是
        """
        if x == -1:
            return -1 if n % 2 else 1
        if x == 1:
            return 1
        if n == -2147483648:
            return 0

        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)

        if n & 1 == 1:
            return x * self.myPow(x, n - 1)
        return self.myPow(x, n >> 1) ** 2


if __name__ == '__main__':
    print(Solution().myPow(2.0, 21))