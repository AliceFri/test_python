"""
冒泡排序：
每一轮 谁大谁往后， 确定一个最大的数放到最左边
"""
import random


def BubbleSort(arr):
    for i in range(len(arr) - 1, -1, -1):
        for a in range(i):
            if arr[a] > arr[a + 1]:
                arr[a], arr[a + 1] = arr[a + 1], arr[a]

    return arr


if __name__ == '__main__':
    print(BubbleSort([random.randint(1, 100) for _ in range(20)]))