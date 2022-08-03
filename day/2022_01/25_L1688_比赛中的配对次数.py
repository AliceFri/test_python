# 数学 直接等于 n - 1
def numberOfMatches(n: int) -> int:
    if n <= 2:
        return n - 1
    iMatch = n // 2
    iLeft = n % 2
    return iMatch + numberOfMatches(iMatch + iLeft)


if __name__ == '__main__':
    print(numberOfMatches(7))
    print(numberOfMatches(14))