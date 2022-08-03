# 累加数

# 回溯

# 1. 遍历确定第一个字符和第二个字符
# 2. 字符串加法 避免溢出
# 3. 数字不以0开头，除了0

def isAdditiveNumber(num: str) -> bool:
    """

    :param num:
    :return:
    """
    def stringAdd(sFirst, sSecond):
        # return str(int(sFirst) + int(sSecond))
        # 模拟加法
        sRFirst, sRSecond = sFirst[::-1], sSecond[::-1]
        lRes = []
        iFirst, iSecond = 0, 0
        iFLen, iSLen = len(sFirst), len(sSecond)
        carry = 0
        iBase = ord('0')
        while iFirst < iFLen or iSecond < iSLen or carry:
            cur = carry
            if iFirst < iFLen:
                cur = cur + ord(sRFirst[iFirst]) - iBase
                iFirst += 1
            if iSecond < iSLen:
                cur = cur + ord(sRSecond[iSecond]) - iBase
                iSecond += 1
            carry = cur // 10
            lRes.append(chr(cur % 10 + iBase))
        return ''.join(lRes[::-1])

    def valid(sFirst, sSecond, iSEnd):
        iLen = len(num)
        while iSEnd <= iLen - 1:
            sThird = stringAdd(sFirst, sSecond)
            iThird = len(sThird)
            if num[iSEnd:iSEnd+iThird] != sThird:
                return False
            sFirst, sSecond = sSecond, sThird
            iSEnd = iSEnd + iThird
            if iSEnd == iLen:       # 刚好匹配完全
                return True
        return False

    iLen = len(num)
    if iLen <= 2:
        return False
    iFStart, iFEnd = 0, 1   # 左开右闭
    iSEnd = 2
    for iFEnd in range(1, iLen - 1):
        sFirst = num[iFStart:iFEnd]
        if iFEnd - iFStart >= 2 and sFirst.startswith('0'):     # 去除以0开头的长度大于2的数字
            continue
        for iSEnd in range(iFEnd + 1, iLen):
            sSecond = num[iFEnd:iSEnd]
            if iSEnd - iFEnd >= 2 and sSecond.startswith('0'):
                continue
            if valid(sFirst, sSecond, iSEnd):
                return True
    return False


def isAdditiveNumber1(num: str) -> bool:
    def dfs(iIndex, sFirst, sSecond):
        iLen = len(num)
        if iIndex >= iLen:  # 全部匹配上了
            return True
        sThird = str(int(sFirst) + int(sSecond))
        iThirdIndex = iIndex + len(sThird)
        if num[iIndex: iThirdIndex] == sThird:
            sFirst, sSecond = sSecond, sThird

            return dfs(iThirdIndex, sFirst, sSecond)
        return False

    iLen = len(num)
    for iFEnd in range(1, iLen - 1):
        sFirst = num[0: iFEnd]
        if iFEnd != 1 and sFirst.startswith('0'):
            return False
        for iSEnd in range(iFEnd + 1, iLen):
            sSecond = num[iFEnd: iSEnd]
            if len(sSecond) != 1 and sSecond.startswith('0'):
                break
            if dfs(iSEnd, sFirst, sSecond):
                return True
    return False


if __name__ == '__main__':
    print(isAdditiveNumber1('198019823962'))
    # print(isAdditiveNumber1('199100199'))
    # print(isAdditiveNumber1('211738'))