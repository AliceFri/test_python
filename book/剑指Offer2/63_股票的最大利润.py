"""
Mid

假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        iMin = None
        for i in prices:
            if iMin is None:
                iMin = i
            profit = max(profit, i - iMin)
            iMin = min(iMin, i)
        return profit