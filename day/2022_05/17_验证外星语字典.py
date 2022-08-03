from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lChar = [0] * 26
        for i, c in enumerate(order):
            lChar[ord(c) - ord('a')] = i

        def IsBigger(w1: str, w2: str) -> bool:
            nonlocal lChar
            if w2.startswith(w1):
                return True
            if not w1:
                return True
            if not w2:
                return False

            iCmp = lChar[ord(w2[0]) - ord('a')] - lChar[ord(w1[0]) - ord('a')]
            if iCmp > 0:
                return True
            elif iCmp < 0:
                return False
            return IsBigger(w1[1:], w2[1:])

        for i in range(len(words) - 1):
            if IsBigger(words[i], words[i + 1]):
                continue
            return False
        return True


if __name__ == '__main__':
    print(Solution().isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
    print(Solution().isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
    print(Solution().isAlienSorted(["apple","app"], "worldabcefghijkmnpqstuvxyz"))

