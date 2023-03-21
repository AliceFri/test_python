from functools import cache
from typing import List


class Solution1:
    # 233题， 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
    def countDigitOne(self, n: int) -> int:
        l = list(str(n))
        ll = len(l)

        # i: 选择第 i 位数
        # is_limit: 前面选择的前缀是否和 n 相同，若相同， 则可选择范围为 0-l[i], 否则为 0-9
        # is_num:   表示前面是否选过数， 避免前导 0 影响
        # 其他: 这里可以加个 oneCnt: 记录前面1的个数
        @cache
        def f(i: int, is_limit: bool, is_num: bool, onecnt: int):
            if i >= ll:
                return onecnt

            up = int(l[i]) if is_limit else 9

            ians = 0
            for choose in range(up + 1):
                ians += f(
                    i + 1,
                    is_limit and choose == up,
                    choose != 0 or is_num,
                    onecnt + (choose == 1),
                )

            return ians

        return f(0, True, False, 0)

    # 600题，给定一个正整数 n ，请你统计在 [0, n] 范围的非负整数中，有多少个整数的二进制表示中不存在 连续的 1 。
    def findIntegers(self, n: int) -> int:
        l = list(bin(n)[2:])

        # 不需要 is_num, 需要加个参数 pre 记录前一位 选择的 0/1
        @cache
        def f(i: int, is_limit: True, pre: int) -> int:
            if i >= len(l):
                return 1
            up = 1 if not is_limit else int(l[i])
            ians = 0
            for choose in range(up + 1):
                if pre == 1 and choose == 1:
                    continue  # 避免连续的 1
                ians += f(i + 1, is_limit and choose == up, choose)
            return ians

        return f(0, True, 0)

    # 902题: 给定一个按非递减顺序排列的数字数组digits 。你可以用任意次数digits[i]来写的数字。例如，如果digits = ['1', '3', '5']，我们可以写数字，如'13', '551', 和'1351315'。
    # 返回可以生成的小于或等于给定整数 n 的正整数的个数
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        l = list(str(n))
        print(l)

        # 需要 is_num 避免 digits 没有 0 选不到 0 ， 如果 digits 可以选0，不需要is_num, 且注意是否需要去除0的影响
        @cache
        def f(i: int, is_limit: bool, is_num: bool):
            if i >= len(l):
                return int(is_num)
            ians = 0
            if not is_num:
                ians += f(i + 1, False, False)
            for d in digits:
                if is_limit and int(d) > int(l[i]):  # 不能选
                    continue
                ians += f(i + 1, is_limit and int(d) == int(l[i]), True)
            return ians

        return f(0, True, False)

    # 面试题 编写一个方法，计算从0到n(含n) 中数字2出现的次数。
    def numberOf2sInRange(self, n: int) -> int:
        l = list(str(n))

        @cache
        def f(i: int, is_limit: bool, twoCnt: int) -> int:
            if i >= len(l):
                return twoCnt
            up = int(l[i]) if is_limit else 9
            ians = 0
            for choose in range(up + 1):
                ians += f(i + 1, is_limit and choose == up, twoCnt + (choose == 2))
            return ians

        return f(0, True, 0)


if __name__ == '__main__':
    s = Solution1()
    print(s.findIntegers(1))
    print(s.atMostNGivenDigitSet(["1", "3", "5", "7"], 100))
    print(s.numberOf2sInRange(25))
