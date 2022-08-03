from typing import List

# 可以用二维dp优化 dp[i][j] 代表最后两位是 第i位和第j位的 最大数
# dp[i][j] = dp[j][k] + 1


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        sArr = set(arr)

        iMax = 0
        for a in range(len(arr) - 2):
            if len(arr) - a + 1 <= iMax:
                break
            for b in range(a + 1, len(arr) - 1):
                if len(arr) - b + 1 <= iMax:
                    break
                iT = 2
                a1, b1 = arr[a], arr[b]
                c = a1 + b1
                while c in sArr:
                    iT += 1
                    b1, c = c, c + b1
                if iT > 2 and iT > iMax:
                    iMax = iT

        return iMax


# 最长的斐波那契子序列的长度