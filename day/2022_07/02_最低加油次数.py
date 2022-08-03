from typing import List

# 最差的方法 深度遍历，dfs 2的n次方时间复杂度 n为stations的长度
# 其次的方法 动态规划 dp[a][b] 代表前a个加油站加b次油能达到的最远距离
# dp[a][b] = dp[a - 1][b]
# if dp[a - 1][b - 1] >= stations[a - 1][0]:
#    dp[a][b] = max(dp[a][b], dp[a - 1][b - 1] + stations[a - 1][1])
# O(n方) n为stations的长度

# 最好的方法 用拿油但不用油, 每次没油了,从经过的加油站拿油最多的一次来用. 这样到达终点加油次数最小,或者不能达到终点.
# 贪心 + 堆 O(n lg n)


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0

        i = len(stations) + 1

        dp = [[0] * i for _ in range(i)]

        for a in range(i):
            dp[a][0] = startFuel

        iRet = None

        for a in range(1, i):
            for b in range(1, a + 1):
                dp[a][b] = dp[a - 1][b]
                if dp[a - 1][b - 1] >= stations[a - 1][0]:
                    dp[a][b] = max(dp[a][b], dp[a - 1][b - 1] + stations[a - 1][1])
                if dp[a][b] >= target:
                    if iRet is None:
                        iRet = b
                    iRet = min(iRet, b)

        if iRet is None:
            return -1
        return iRet

        # minTime = None

        # def addAnswer(i):
        #     nonlocal minTime
        #     if minTime is None:
        #         minTime = i
        #     minTime = min(minTime, i)

        # tations = [[0, 0]] + stations 

        # def dfs(i, fuel, time): # 到达第几个加油站
        #     if minTime != None and time >= minTime:
        #         return 
        #     loc, addfuel = stations[i]
        #     if loc + fuel >= target:
        #         addAnswer(time)
        #         return

        #     if i == len(stations) - 1:  # 最后一个加油站
        #         if loc + fuel + addfuel >= target:
        #             addAnswer(time + 1)
        #         return

        #     nloc = stations[i + 1][0]
        #     if loc + fuel >= nloc:
        #         dfs(i + 1, fuel - (nloc - loc), time)
        #     if loc + fuel + addfuel >= nloc and addfuel > 0:
        #         dfs(i + 1, fuel + addfuel - (nloc - loc), time + 1)

        # dfs(0, startFuel, 0)
        # if minTime is None:
        #     return -1
        # return minTime



