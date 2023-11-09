from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSon(s1, s2):
            if len(s1) > len(s2):
                return False
            i = 0
            p1, p2 = 0, 0
            while p1 < len(s1) and p2 < len(s2):
                if s2[p2] == s1[p1]:
                    p1 += 1
                    p2 += 1
                    i += 1
                else:
                    p2 += 1
            return i == len(s1)

        strs.sort(key=lambda x: len(x))

        for i in range(len(strs) - 1, -1, -1):
            b = True
            for ii in range(0, len(strs)):
                if i == ii:
                    continue
                if isSon(strs[i], strs[ii]):
                    b = False
                    break
            if b:
                return len(strs[i])

        return -1