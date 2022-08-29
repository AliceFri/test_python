"""
Mid

给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
"""

class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        l = len(str(num))
        dp = [1] * (l + 1)
        for i in range(1, l):
            if num[i - 1] == '0' or num[i - 1] > '2' or (num[i - 1] == '2' and num[i] >= '6'):
                dp[i + 1] = dp[i]
            else:
                dp[i + 1] = dp[i] + dp[i - 1]

        return dp[-1]


if __name__ == '__main__':
    print(Solution().translateNum(12258))