"""
aabcb -> 5
aabcbaa -> 17
"""


class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        dp = [[0] * 26 for _ in range(n + 1)]
        pre = [0] * 26
        for i in range(n):
            c = s[i]
            pre[ord(c) - ord('a')] += 1
            for a in range(26):
                dp[i + 1][a] = pre[a]

        ans = 0
        for a in range(n - 1):
            for b in range(a + 1, n):
                tmp = [dp[b + 1][i] - dp[a][i] for i in range(26)]
                tmp = [i for i in tmp if i]
                m = max(tmp)
                mi = min(tmp)
                if mi > 0:
                    ans += m - mi
        return ans


if __name__ == '__main__':
    print(Solution().beautySum("aabcb"))
    print(Solution().beautySum("aabcbaa"))
