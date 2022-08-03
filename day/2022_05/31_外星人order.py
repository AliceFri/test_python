from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:

        count = {}
        for i in words[0]:
            count[i] = []
        for i in range(1,len(words)):
            for j in words[i]:
                count.setdefault(j, [])
            for j in range(min(len(words[i-1]),len(words[i]))):
                if words[i][j] != words[i-1][j]:
                    count[words[i-1][j]].append(words[i][j])
                    break
            else:
                if len(words[i-1]) > len(words[i]):
                    return ""

        VISITING, VISITED = 1, 2
        states = {}
        ans = []
        def dfs(u):
            states[u] = VISITING
            for i in count[u]:
                if i not in states:
                    t = dfs(i)
                    if t == False:
                        return False
                elif states[i] == VISITING:
                    return False
            ans.append(u)
            states[u] = VISITED
            return True

        for i in count:
            if i not in states:
                if not dfs(i):
                    return ""

        return "".join(reversed(ans))


if __name__ == '__main__':
    print(Solution().alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
