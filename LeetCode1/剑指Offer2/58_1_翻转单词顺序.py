"""
Easy

"""


class Solution:
    def reverseWords(self, s: str) -> str:
        # l = s.split(' ')
        # l = [i for i in l if i]
        # return ' '.join(l[::-1])
        # l = s.split()
        return " ".join(reversed(s.split()))

    def reverseLeftWords(self, s: str, n: int) -> str:  # 整体翻转 + 两次局部翻转
        n = n % len(s)
        return s[n:] + s[:n]


if __name__ == '__main__':
    print(Solution().reverseWords("a good   example"))
    print(Solution().reverseLeftWords("agoodexample", 2))