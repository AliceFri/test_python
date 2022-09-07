"""
Mid

把字符串转换成整数
"""
class Solution:
    def strToInt(self, s: str) -> int:
        flag = 1
        nums = []
        begin = True
        d = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
        }
        for c in s:
            if c == ' ' and begin:
                continue
            if c in ('-', '+'):
                if not begin:
                    break
                begin = False
                flag = 0 if c == '-' else 1
            elif c in d:
                begin = False
                nums.append(d[c])
            else:
                break

        if not nums:
            return 0

        i = 0
        x = 1
        for c in nums[::-1]:
            i += x * c
            x *= 10
        if not flag:
            i = -i
        i = min(i, 2 ** 31 - 1)
        i = max(i, -(2 ** 31))
        return i


if __name__ == '__main__':
    print(Solution().strToInt("42"))
    print(Solution().strToInt("-42"))
    print(Solution().strToInt("-42dafa"))
    print(Solution().strToInt("    -42dafa"))
    print(Solution().strToInt("    --42dafa"))
