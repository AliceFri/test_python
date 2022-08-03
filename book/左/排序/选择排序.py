"""
选择排序：
每轮 找到一个最小值, 然后交换到当前最左边的位置。
"""
import random


def selection_sort(arr):
    for a in range(0, len(arr) - 1):
        iMinInd = a
        for b in range(a + 1, len(arr)):
            if arr[b] < arr[iMinInd]:
                iMinInd = b

        arr[a], arr[iMinInd] = arr[iMinInd], arr[a]

    return arr


if __name__ == '__main__':
    print(selection_sort([random.randint(1, 100) for i in range(20)]))