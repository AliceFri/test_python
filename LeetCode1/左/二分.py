# 二分查抄

def ef_search(arr, i):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (r - l) // 2 + l

        if arr[mid] == i:
            return mid
        elif arr[mid] < i:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def ef_search_left(arr, i):
    l, r = 0, len(arr) - 1
    iRet = -1
    while l <= r:
        mid = (r - l) // 2 + l
        if arr[mid] > i:
            r = mid - 1
        elif arr[mid] < i:
            l = mid + 1
        else:
            iRet = mid
            r = mid - 1

    return iRet


def ef_search_right(arr, i):
    l, r = 0, len(arr) - 1
    iRet = -1
    while l <= r:
        mid = (r - l) // 2 + l
        if arr[mid] > i:
            r = mid - 1
        elif arr[mid] < i:
            l = mid + 1
        else:
            iRet = mid
            l = mid + 1
    return iRet


# 局部最小值 len(arr) >= 2, arr中数各不相等
def oneMinInd(arr):
    if arr[0] < arr[1]:
        return 0
    if arr[-1] < arr[-2]:
        return len(arr) - 1

    l, r = 1, len(arr) - 2
    while l <= r:
        m = (r - l) // 2 + l
        if arr[m - 1] > arr[m] < arr[m + 1]:
            return m

        if arr[m - 1] < arr[m]:
            r = m - 1
        else:
            l = m + 1
    return -1


if __name__ == '__main__':
    print(ef_search_left([1, 1, 2, 3, 3, 3, 4, 5, 20], 3))
    print(ef_search_left([1, 1, 2, 3, 3, 3, 4, 5, 20], 1))
    print(ef_search_right([1, 1, 2, 3, 3, 3, 4, 5, 20], 3))
    print(ef_search_right([1, 1, 2, 3, 3, 3, 4, 5, 20], 1))
    print(ef_search_right([1, 1, 2, 3, 3, 3, 4, 5, 20], 2))
    print(ef_search_right([1, 1, 2, 3, 3, 3, 4, 5, 20], 2))
    print(ef_search_right([1, 1, 2, 3, 3, 3, 4, 5, 20], 21))
    print(ef_search_right([1, 1, 2, 3, 3, 3, 4, 5, 20], 21))
    print(oneMinInd([3, 2, 1, 4, 5, 6, 7, 8, 9]))
    print(oneMinInd([3, 2, 3, 2, 3]))