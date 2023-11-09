# 最小时间差


# 排序, 计算最小值
def findMinDifference(timePoints: list) -> int:
    # 容斥原理
    if len(timePoints) >= 1440:
        return 0

    timePoints.sort()

    def GetSubSecond(t1, t2):
        h1, m1 = [int(i) for i in t1.split(":")]
        h2, m2 = [int(i) for i in t2.split(":")]
        i = h1 * 60 + m1 - (h2 * 60 + m2)
        return min(i, 1440 - i)

    iMin = GetSubSecond(timePoints[-1], timePoints[0])
    for index in range(1, len(timePoints)):
        iMin = min(iMin, GetSubSecond(timePoints[index], timePoints[index-1]))
        if iMin <= 0:
            return 0
    return iMin


if __name__ == '__main__':
    print(findMinDifference(["00:00", "04:00", "22:00"]))
    print(findMinDifference(["23:59", "00:00", "23:59"]))