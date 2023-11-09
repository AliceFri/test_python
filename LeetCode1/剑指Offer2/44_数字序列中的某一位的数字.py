"""
Mid

数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。
"""

class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        return self._find(n + 1)

    def getNumsByDigit(self, digit: int) -> int:
        if digit == 1:
            return 10
        return 10 ** (digit - 1) * 9

    def _find(self, n):
        # 先确定是几位数， 再确定是哪个数， 再确定是那个数的第几位
        digit = 1
        while n > self.getNumsByDigit(digit) * digit:
            n -= self.getNumsByDigit(digit) * digit    # digit位数 总长度=数的个数 * digit
            digit += 1

        # 确定是哪个数
        nums = 10 ** (digit - 1) + (n - 1) // digit

        return int(str(nums)[(n - 1) % digit])


if __name__ == '__main__':
    print(Solution().findNthDigit(1000))