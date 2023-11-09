"""
Easy

编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为 汉明重量).）。
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        限制输入正数
        """
        # iCnt = 0
        # while n:
        #     if n & 1:
        #         iCnt += 1
        #     n = n >> 1
        # return iCnt

        # 1. 循环检查二进制位
        # ret = sum(1 for i in range(32) if n & (1 << i))

        # 2. 位运算优化
        # n & (n−1)，其预算结果恰为把n的二进制位中的最低位的1变为0之后的结果
        # ret = 0
        # while n:
        #     n &= n - 1
        #     ret += 1
        # return ret

        # lowbit n & -x  返回二进制表示中最低位 1 所表示的数值
        # ret = 0
        # while n:
        #     n -= (n & -n)
        #     ret += 1

        # 分组统计
        n = (n & 0x55555555) + ((n >> 1) & 0x55555555)
        n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
        n = (n & 0x0f0f0f0f) + ((n >> 4) & 0x0f0f0f0f)
        n = (n & 0x00ff00ff) + ((n >> 8) & 0x00ff00ff)
        n = (n & 0x0000ffff) + ((n >> 16) & 0x0000ffff)
        return n


if __name__ == '__main__':
    n = 33
    print(bin(n))
    print(sum(1 for i in range(32) if n & (1 << i)))
    print(Solution().hammingWeight(n))
