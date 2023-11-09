def simplifiedFractions(n: int) -> list:
    dRet = {}  # value: 字符串

    for a in range(2, n + 1):
        for b in range(1, a):
            if b / a in dRet:
                continue
            dRet[b / a] = "%s/%s" % (b, a)

    return list(dRet.values())


if __name__ == '__main__':
    print(simplifiedFractions(4))