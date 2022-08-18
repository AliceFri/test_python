"""
Easy

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
"""

class Solution:
    def replaceSpace(self, s: str) -> str:
        d = [c if c != ' ' else '%20' for c in s]
        return ''.join(d)


if __name__ == '__main__':
    print(Solution().replaceSpace("we happy"))