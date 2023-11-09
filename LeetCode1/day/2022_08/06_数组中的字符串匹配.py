from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))

        res = []
        for a in range(len(words) - 1):
            for b in range(a + 1, len(words)):
                if words[a] in words[b]:
                    res.append(words[a])
                    break

        return res
