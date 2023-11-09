"""
Easy


"""
from functools import cache


class Solution:
    @cache
    def fib(self, n: int) -> int:
        """
        动态规划 / 记忆化递归
        """
        """
        动态规划不用保留过去的所有值，只需要保留前两项 (优化点)
        矩阵快速mi算法。 
        """
        if n in (0, 1):
            return n
        return (self.fib(n - 1) + self.fib(n - 2)) % 1000000007