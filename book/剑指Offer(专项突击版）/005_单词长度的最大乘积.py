class Solution:
    def maxProduct(self, words: List[str]) -> int:

        lSet = [set(word) for word in words]

        # 集合可以用 二进制替代
        iRet = 0
        for a in range(0, len(words) - 1):
            for b in range(a + 1, len(words)):
                s1, s2 = lSet[a], lSet[b]
                iMatch = 1
                for s in s1:
                    if s in s2:
                        iMatch = 0
                        break

                if iMatch:
                    iRet = max(iRet, len(words[a]) * len(words[b]))

        return iRet

