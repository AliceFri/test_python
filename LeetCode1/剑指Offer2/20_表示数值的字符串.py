"""
Mid

（可选）一个符号字符（'+' 或 '-'）
下述格式之一：
至少一位数字，后面跟着一个点 '.'
至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
一个点 '.' ，后面跟着至少一位数字
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        def fix(s):  # 去除首尾空格
            a = 0
            b = len(s)
            for i in range(len(s)):
                if s[i] == ' ':
                    a += 1
                else:
                    break
            if a >= len(s):
                return ""
            for i in range(len(s) - 1, -1, -1):
                if s[i] == ' ':
                    b -= 1
                else:
                    break
            return s[a:b]

        s = fix(s)
        if s == "":
            return False

        canPoint = True
        canFlag = True
        canE = -1  # 只有为0时才能加e
        needNumber = True

        for i in s:

            if i in ('+', '-'):
                if not canFlag:
                    return False
                canFlag = False
            elif i == '.':
                if not canPoint:
                    return False
                canPoint = False
                canFlag = False
            elif i in ('e', 'E'):
                if canE != 0:
                    return False
                canE += 1
                canPoint = False
                canFlag = True
                needNumber = True

            elif 0 <= ord(i) - ord('0') <= 9:
                canFlag = False
                needNumber = False
                if canE == -1:
                    canE = 0

            else:
                return False

        if needNumber:
            return False
        return True


if __name__ == '__main__':
    print(Solution().isNumber('+100'))
    print(Solution().isNumber('5e2'))
    print(Solution().isNumber('-123'))
    print(Solution().isNumber('3.1416'))
    print(Solution().isNumber('-1E-2'))
    print(Solution().isNumber('0123'))

    print(Solution().isNumber('12e'))
    print(Solution().isNumber('1a3.14'))
    print(Solution().isNumber('+-5'))
    print(Solution().isNumber('12e+5.4'))
