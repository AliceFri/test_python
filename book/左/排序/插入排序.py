"""
插入排序

打牌， 每一轮，多保持一个数有序
"""
import random


def insertSort(arr):
    for a in range(1, len(arr)):
        for b in range(a, 0, -1):
            if arr[b] >= arr[b - 1]:
                break
            arr[b], arr[b - 1] = arr[b - 1], arr[b]

    return arr


if __name__ == '__main__':
    print(insertSort([random.randint(1, 100) for _ in range(20)]))