"""
Mid

请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
"""

"""
滑动窗口
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        a, b = 0, 0
        res = 1
        visited = {s[0]: 0}

        for i in range(1, len(s)):
            b = i
            if s[i] not in visited:
                visited[s[i]] = i
                res = max(res, b - a + 1)
            else:
                for c in range(a, visited[s[i]]):
                    visited.pop(s[c])
                a = visited[s[i]] + 1
                visited[s[i]] = i
        return res


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
    print(Solution().lengthOfLongestSubstring("tmmzuxt"))