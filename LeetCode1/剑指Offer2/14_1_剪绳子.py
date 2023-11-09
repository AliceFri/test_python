"""
Mid

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。
请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/jian-sheng-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from functools import cache


class Solution:
    """
    1. 动态规划
    2. 贪心算法：
    最优： 3 。把绳子尽可能切为多个长度为 3 的片段，留下的最后一段绳子的长度可能为 0,1,2 三种情况。
    次优： 2 。若最后一段绳子长度为 2 ；则保留，不再拆为 1+1 。
    最差： 1 。若最后一段绳子长度为 1 ；则应把一份 3 + 1 替换为 2 + 2，因为2 × 2 > 3 × 1。
    """

    @cache
    def cuttingRope(self, n: int) -> int:
        # iMax = 1
        # for i in range(1, n):
        #     iMax = max(iMax, i * self.cuttingRope(n - i), i * (n - i))
        # return iMax

        dp = [0] * (n + 1)  # 建立空间
        dp[0] = dp[1] = 1  # 初始值
        for i in range(2, n + 1):
            for c in range(1, (i >> 1) + 1):  # 可证明减前半段优于后半段
                dp[i] = max(dp[i], c * (i - c), c * dp[i - c])
        # print(dp)
        return dp[-1] % 1000000007


if __name__ == '__main__':
    print(Solution().cuttingRope(10))
