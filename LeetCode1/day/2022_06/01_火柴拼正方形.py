from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        iSum = sum(matchsticks)
        if iSum % 4 != 0:
            return False
        matchsticks.sort(reverse=True)

        iSide = iSum / 4

        dSum = [0, 0, 0, 0]
        res = False

        def dfs(i):
            nonlocal res
            if i >= len(matchsticks):
                if dSum[0] == dSum[1] == dSum[2] == dSum[3] == iSide:
                    res = True
                    return True
                return False
            for a in range(4):
                if dSum[a] + matchsticks[i] <= iSide:
                    dSum[a] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    dSum[a] -= matchsticks[i]
            return False

        dfs(0)
        return res