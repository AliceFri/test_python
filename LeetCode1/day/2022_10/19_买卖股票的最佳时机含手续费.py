# 输入：prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出：8
# 解释：能够达到的最大利润:
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8
from typing import List


# 输入：prices = [1,3,7,5,10,3], fee = 3
# 输出：6


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][-1] = -(prices[0] + fee)

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)

        return max(dp[-1])


if __name__ == '__main__':
    print(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2))
    print(Solution().maxProfit([1, 3, 7, 5, 10, 3], 3))
