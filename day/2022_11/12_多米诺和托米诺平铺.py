# dp[1] = 1
# dp[2] = 2

# dp[3] = 5

# dp[4] = dp[1] * dp[3] + dp[2]


"""
分成 x 份

总长度 应在 limit * (x - 1) -- limit * x

假设 x 为 1 位数；
    总长度为 len(message) + 5 * x

假设 x 为 2 位数：
    总长度 为 len(message) + 6 * 9 + (x - 9) * 7

假设 x 为 3 位数：
    总长度 为 len(message) + 7 * 9 + 8 * 90  + 9 * (x - 99)

总长度 x 为 4 位数:
    总长度 为 len(message) + 8 * 9 + 9 * 90 + 10 * 900 + 11 * (x - 999)



"""
from functools import lru_cache


class Solution:
    def numTilings(self, n: int) -> int:
        @lru_cache
        def get_weight(top, bottom):
            if top == 0 and bottom == 0:
                return 1
            i = 0
            if top & 1:
                if bottom & 1:
                    i += get_weight(top >> 1, bottom >> 1)
                if (top >> 1) & 1:
                    i += get_weight(top >> 2 << 2, bottom)
                if (top >> 1) & 1 and (bottom >> 1) & 1 and not (bottom & 1):
                    i += get_weight(top >> 2, bottom >> 2)
                if bottom & 1 and (top >> 1) & 1:
                    i += get_weight(top >> 2 << 1, bottom >> 1)
                if bottom & 1 and (bottom >> 1) & 1:
                    i += get_weight(top >> 1, bottom >> 2 << 1)
                return i
            if not bottom & 1:
                return get_weight(top >> 1, bottom >> 1)
            i = 0
            if (bottom >> 1) & 1:
                i += get_weight(top >> 1, bottom >> 2 << 1)
            if (bottom >> 1) & 1 and (top >> 1) & 1:
                i += get_weight(top >> 2, bottom >> 2)
            return i

        return get_weight(2 ** n - 1, 2 ** n - 1) % (10 ** 9 + 7)


if __name__ == "__main__":
    print(Solution().numTilings(3))
