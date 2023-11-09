"""
Easy

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

约瑟夫 环
f(n, m) = (m % n) + f(n - 1, m) = (m + f(n - 1, m)) % n

f(5, 3) = 3 + f(4, 3)
        = 3 + 3 + f(3, 3)
        = 3 + 3 + 0 + f(2, 3)
        = 3 + 3 + 0 + 1 + 0
        = 3 + 3 + 0 + 1 % 2
        = 3 + 3 + 1 % 3
        = 3 + 4 % 4
        = 3 % 5
        = 3
"""


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        ret = 0
        for i in range(2, n + 1):
            ret = (m + ret) % i

        return ret


if __name__ == '__main__':
    print(Solution().lastRemaining(10, 17))
