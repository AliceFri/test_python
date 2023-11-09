class Solution:
    def nextGreaterElement(self, n: int) -> int:
        ns = [int(i) for i in str(n)]

        i = len(ns) - 2
        while i >= 0 and ns[i] >= ns[i + 1]:
            i -= 1

        # i 为将要换的那个位置eg:1238765432 这里的第一个3的位置
        if i < 0:
            return -1

        j = len(ns) - 1
        while j >= i and ns[j] <= ns[i]:
            j -= 1
        # j为要更换的第二个位置 eg 1238765432 这里的4, 即大于i(3)的最右边的那个数

        ns[i], ns[j] = ns[j], ns[i] # 124 8765332

        ns[i+1:] = ns[i+1:][::-1]   # 第i位之后的数 反转 124 2335678

        i = int(''.join([str(i) for i in ns]))

        if i > 2 ** 31 - 1:
            return -1
        return i

