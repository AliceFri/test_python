

# 1. 全部字母均为大写 True
# 2. 全部字母均为小写 True
# 3. 只有首字母大写 True
def IsWordSpellRight(word):
    if not word:
        return False
    bBigFlag = False    # 大写标记
    bSmallFlag = False  # 小写标记

    cFirst = word[0]
    if 0 <= ord(cFirst) - ord('a') < 26:
        bSmallFlag = True

    for ind in range(1, len(word)):
        s = word[ind]
        if 0 <= ord(s) - ord('A') < 26:
            if bSmallFlag:
                return False
            bBigFlag = True
        elif 0 <= ord(s) - ord('a') < 26:
            if bBigFlag:
                return False
            bSmallFlag = True
        else:
            return False

    return True


if __name__ == '__main__':
    print(IsWordSpellRight('USA'))
    print(IsWordSpellRight('AabcdDefghijklmnopqrstuvwxyz'))
    print(IsWordSpellRight('uF'))