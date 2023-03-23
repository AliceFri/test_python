# 状态机解法 DFA, 有限字符集, O(MN)   M是字符集个数， N是操作字符串的长度
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # 1. 构造状态表, 26个字符串, len(needle) + 1 个状态
        dp = [[0] * 26 for _ in range(len(needle) + 1)]

        # 1.1 初始状态
        dp[0][ord(needle[0]) - ord('a')] = 1  # 0号状态碰到needle[0], 变为1号状态； 碰到其他字符还是0号状态
        X = 0  # 影子状态
        # 1.2 构建状态表
        for i in range(1, len(dp)):
            for a in range(26):
                if i < len(needle) and ord(needle[i]) - ord('a') == a:
                    dp[i][a] = i + 1
                else:
                    dp[i][a] = dp[X][a]
                # 更新影子状态
            if i < len(needle):
                X = dp[X][ord(needle[i]) - ord('a')]

        ans = []  # 全部匹配下标

        cur = 0  # 当前状态
        # 2. 状态转移
        for i in range(len(haystack)):
            cur = dp[cur][ord(haystack[i]) - ord('a')]
            if cur == len(dp) - 1:  # 到达目标状态
                ans.append(i - len(needle) + 1)

        if not ans:
            return -1
        return ans[0]


def build_next(patt):
    """
    生成 Next 数组
    """

    _next = [0]  # next 数组 (初值元素一个 0)
    prefix_len = 0  # 当前共同前后缀的长度
    i = 1
    while i < len(patt):
        if patt[prefix_len] == patt[i]:
            prefix_len += 1
            _next.append(prefix_len)
            i += 1
        else:
            if prefix_len == 0:
                _next.append(prefix_len)
                i += 1
            else:
                prefix_len = _next[prefix_len - 1]

    return _next


def kmp_search(string, patt):
    """
    在 string 中搜索 patt。如果匹配成功则返回第一个匹配的位置
    """

    _next = build_next(patt)  # 假设我们已经知道了 next 数组 (马上讲到)

    i = 0  # 主串的指针
    j = 0  # 子串的指针
    while i < len(string):
        if string[i] == patt[j]:  # 字符匹配，指针后移
            i += 1
            j += 1
        elif j > 0:  # 字符失配，根据 next 跳过部分字符的匹配
            j = _next[j - 1]
        else:  # patt[0] 就失配了，直接比较主串的下一个字符
            i += 1

        if j == len(patt):  # 子串匹配成功
            return i - j

    return -1


if __name__ == '__main__':
    s = Solution()
    # print(s.strStr("sadbutsad", "sad"))
    print(s.strStr("aaabaaabbbabaa", "babb"))

    print(build_next("ABACABAB"))
