"""
Easy

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
"""

class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return ' '
        multi = set()
        first = {}
        for i in range(len(s)):
            c = s[i]
            if c in multi:
                continue
            if c in first:
                first.pop(c)
                multi.add(c)
                # if len(multi) == 25:
                #     return [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in multi][0]
            else:
                first[c] = i

        res_i = None
        res_c = " "
        for c, i in first.items():
            if res_i is None or i < res_i:
                res_c = c
                res_i = i
        return res_c


if __name__ == '__main__':
    print(Solution().firstUniqChar("yekbsxznylrwamcaugrqrurvpqybkpfzwbqiysrdnrsnbftvrnszfjbkbmrctjizkjqoxqzddyfnavnhqeblfmzqgsjflghaulbadwqsyuetdelujphmlgtmkoaoijypvcajctbaumeromgejtewbwqptotrorephegyobbstvywljboeihdliknluqdpgampjyjpinxhhqexoctysfdciqjbzilnodzoihihusxluqoayenluziobxiodrfdkinkzzozmxfezfvllpdvogqqtquwcsijwachefspywdgsohqtlquhnoecccgbkrzqcprzmwvygqwddnehhi"))