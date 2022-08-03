# dp[i] = dp[i & (i - 1)] + 2

# i & (i - 1)


class Solution:
    def countBits(self, n: int) -> List[int]:
        # def GetOneCount(n):
        #     iAdd = 0

        #     while n:
        #         n = n & (n - 1)
        #         iAdd += 1
        #     return iAdd

        # lRet = [GetOneCount(i) for i in range(n + 1)]

        # return lRet

        # 动态规划
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i & (i - 1)] + 1  # 去掉最低一位1的数 + 1

        return dp