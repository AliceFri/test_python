from typing import List

# 输入: prices = [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [
            [0, 0, 0] for _ in range(len(prices))
        ]  # 0: 无股票， 冷冻期。  1: 无股票， 无冷冻期    2: 有股票

        dp[0][-1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = dp[i - 1][2] + prices[i]
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] - prices[i])

        return max(dp[-1])


if __name__ == '__main__':
    print(Solution().maxProfit([1, 2, 3, 0, 2]))
    print(Solution().maxProfit([1]))
