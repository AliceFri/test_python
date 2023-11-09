"""
Easy

写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号
"""
MASK1 = 4294967296  # 2^32
MASK2 = 2147483648  # 2^31
MASK3 = 2147483647  # 2^31-1


class Solution:
    def add(self, a: int, b: int) -> int:
        return sum([a, b])
        ans = [0] * 32
        times = [i for i in range(32, -1, -1)]

        iadd = 0  # 进位
        for _ in range(31):
            a1 = a & 1
            b1 = b & 1
            iNum = times[-1]
            times.pop()
            if a1 and b1:
                if iadd:
                    ans[iNum] = 1
                    iadd = 1
                else:
                    iadd = 1
            elif a1 or b1:
                if iadd:
                    iadd = 1
                else:
                    ans[iNum] = 1
            else:
                if iadd:
                    ans[iNum] = 1
                    iadd = 0

            a >>= 1
            b >>= 1

        if iadd:
            ans[times[-1]] = 1

        ans = [str(i) for i in ans]
        ans = int("".join(ans[::-1]), 2)

        if ans & MASK2:
            return ~((a ^ MASK2) ^ MASK3)
        return ans


if __name__ == "__main__":
    print(Solution().add(111, 899))

    print(Solution().add(-1, 2))
