# 字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。 
# 
#  
# 
#  示例 1: 
# 
#  输入: 
# first = "pale"
# second = "ple"
# 输出: True 
# 
#  
# 
#  示例 2: 
# 
#  输入: 
# first = "pales"
# second = "pal"
# 输出: False
#  
#  Related Topics 双指针 字符串 👍 164 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first) - len(second)) >= 2:
            return False
        if not first or not second:
            return True

        m, n = len(first), len(second)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1, n + 1):
            dp[0][i] = i
        for i in range(1, m + 1):
            dp[i][0] = i

        for a in range(1, m + 1):
            for b in range(1, n + 1):
                dp[a][b] = min(1 + dp[a][b - 1], 1 + dp[a - 1][b], 1 + dp[a-1][b-1])
                if first[a - 1] == second[b - 1]:
                    dp[a][b] = min(dp[a][b], dp[a - 1][b - 1])
        return dp[m][n] <= 1
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().oneEditAway("teacher", "attacher"))
    # print(Solution().oneEditAway("te", "att"))