# 每个字符都是 a e i o u
# ae
# ea ei
# ii
# oi ou
# ua

# s(n, a) = s(n-1, e)
# s(n, e) = s(n-1, a) + s(n-1, i)
# s(n, i) = s(n-1, a) + s(n-1, e) + s(n-1, o) + s(n-1, u)
# s(n, o) = s(n-1, i) + s(n-1, u)
# s(n, u) = s(n-1, a)

# 自顶向下 + 备忘录
def countVowelPermutation(n: int) -> int:
    uchar = ('a', 'e', 'i', 'o', 'u')
    book = {c: {} for c in uchar}
    next = {
        'a': ('e', ),
        'e': ('a', 'i'),
        'i': ('a', 'e', 'u', 'o'),
        'o': ('i', 'u'),
        'u': ('a',),
    }

    def StartNum(num, char):
        if char in book:
            if num in book[char]:
                return book[char][num]
        if num == 1:
            book[char][num] = 1
            return 1
        tNext = next.get(char, tuple())
        iNum = sum([StartNum(num-1, c) for c in tNext])
        book[char][num] = iNum
        return iNum

    iSum = sum([StartNum(n, c) for c in uchar]) % 1000000007
    return iSum


# 动态规划 自底向上 + 压缩
def countVowelPermutation1(n: int) -> int:
    a, e, i, o, u = 1, 1, 1, 1, 1
    for _ in range(n - 1):
        a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
    return sum([a, e, i, o, u]) % 1000000007
# 数学法


if __name__ == '__main__':
    print(countVowelPermutation1(1))
    print(countVowelPermutation1(2))
    print(countVowelPermutation1(5))