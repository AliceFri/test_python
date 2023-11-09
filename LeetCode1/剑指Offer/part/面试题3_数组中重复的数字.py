# 题目一: 找出数组中重复的数字
# 方法一: 排序， 比较相同的数 nlogn
# 方法二: 集合，字典
# 方法三: 注意到0, n-1。 不断比较下标

def GetDuplicateNum(arr):
    s = set()
    for i in arr:
        if i in s:
            return i
        s.add(i)
    return -1


def GetDuplicateNum2(arr):
    for index, i in enumerate(arr):
        im = index
        m = arr[im]
        while m != im:
            if m == arr[m]:
                return m
            arr[im], arr[m] = arr[m], arr[im]
            m = arr[im]
    return -1


# 题目二 不修改数组找出重复的数字 范围1-n， 长度为n + 1
# 集合, 字典
# 如果需要省空间，则以时间换空间，二分找到重复的数字
def GetDuplicateNum3(arr):
    n = len(arr)

    def CountRange(iLow, iHigh):
        iCount = 0
        for i in arr:
            if iLow <= i <= iHigh:
                iCount += 1
        return iCount > (iHigh - iLow + 1)

    iLow, iHigh = 0, n
    while iLow < iHigh:
        iMid = iLow + (iHigh - iLow) // 2
        if CountRange(iLow, iMid):
            if iMid == iLow:
                return iLow
            iHigh = iMid
        else:
            iLow = iMid + 1
    return iLow


if __name__ == '__main__':
    print(GetDuplicateNum3([1, 2, 3, 4, 3, 5, 5]))