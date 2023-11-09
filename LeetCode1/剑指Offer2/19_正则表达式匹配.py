"""
Hard

. 匹配任意字符， *匹配0个或多个
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        dp[0][0] = True
        for b in range(2, len(p) + 1, 2):
            if p[b - 1] == '*':
                dp[0][b] = dp[0][b - 2]

        for a in range(1, len(s) + 1):
            for b in range(1, len(p) + 1):
                if p[b - 1] == '.' or p[b - 1] == s[a - 1]:
                    dp[a][b] = dp[a - 1][b - 1]
                if p[b - 1] == '*':
                    dp[a][b] = dp[a][b - 2]
                    if p[b - 2] == '.' or p[b - 2] == s[a - 1]:
                        dp[a][b] = dp[a][b] or dp[a - 1][b]
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().isMatch("aab", "c*a*b"))