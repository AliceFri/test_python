class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ans = s
            for i in range(len(s) - 1):
                ans = ans[1:] + ans[0]
                s = min(ans, s)
            return s

        else:
            return ''.join(sorted(s))
