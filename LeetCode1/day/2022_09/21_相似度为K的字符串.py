"""
对于某些非负整数 k ，如果交换 s1 中两个字母的位置恰好 k 次，能够使结果字符串等于 s2 ，则认为字符串 s1 和 s2 的 相似度为 k 。

给你两个字母异位词 s1 和 s2 ，返回 s1 和 s2 的相似度 k 的最小值。
"""

import collections


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:

        d = collections.defaultdict(list)  # {in: [out, out, ...]}

        idiff = 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            d[s1[i]].append(s2[i])
            idiff += 1

        iRes = 0
        while idiff:
            if idiff <= 3:
                iRes += (idiff - 1)
                break
            paths = []
            _set = set()
            # choose start
            for c in ('a', 'b', 'c', 'd', 'e', 'f'):
                if d[c]:
                    paths.append(c)
                    paths.append(d[c][0])
                    _set.add(d[c][0])
                    break

            # 寻找环路      eg: 环不一定最短。。。。

            def _dfs(_in, _target):
                if _target in d[_in]:
                    paths.append(_target)
                    return True
                _s = set()
                for c in d[_in]:
                    if c in _s or c in _set:
                        continue
                    _s.add(c)
                    _set.add(c)
                    paths.append(c)
                    if _dfs(c, _target):
                        return True
                    _set.remove(c)
                    paths.pop(-1)

            _dfs(paths[-1], paths[0])
            print(paths)
            iRes += (len(paths) - 2)
            idiff -= (len(paths) - 1)

            for i in range(1, len(paths)):
                d[paths[i - 1]].remove(paths[i])

        return iRes


if __name__ == '__main__':
    # print(Solution().kSimilarity("ab", "ba"))
    # print(Solution().kSimilarity("abc", "bca"))
    # print(Solution().kSimilarity("abcdefff", "fffedcba"))
    print(Solution().kSimilarity("aabbccddee", "cdacbeebad"))