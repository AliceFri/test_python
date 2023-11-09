import bisect
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        dp = [[] for _ in range(26)]

        for ind, i in enumerate(s):
            dp[ord(i) - ord("a")].append(ind)

        def is_match(w):
            inow = 0
            for c in w:
                l = dp[ord(c) - ord("a")]
                if not l or l[-1] < inow:
                    return False
                itmp = l[bisect.bisect_left(l, inow)]
                inow = itmp + 1
            return True

        print(dp)
        icnt = 0
        for w in words:
            print(w, is_match(w))
            if is_match(w):
                icnt += 1
        return icnt


if __name__ == "__main__":
    print(Solution().numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))
    print(Solution().numMatchingSubseq("dsahjpjauf",  ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))




