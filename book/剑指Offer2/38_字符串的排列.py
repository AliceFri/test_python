"""
Mid

入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
"""
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        iLen = len(s)
        used = [False] * iLen

        res = []

        def dfs(i, l):
            if i == iLen:
                res.append("".join(l))
                return

            _used = set()
            for a in range(iLen):
                if used[a] or s[a] in _used:
                    continue

                l.append(s[a])
                _used.add(s[a])
                used[a] = True
                dfs(i + 1, l)
                l.pop(-1)
                used[a] = False

        dfs(0, [])
        return res


if __name__ == '__main__':
    print(Solution().permutation("abc"))
