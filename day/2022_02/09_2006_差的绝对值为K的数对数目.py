from collections import defaultdict


def countKDifference(nums: list, k: int) -> int:
    dTmp = defaultdict(int)
    count = 0
    for i in nums:
        r1 = k + i
        r2 = i - k
        count += dTmp.get(i, 0)
        dTmp[r1] += 1
        dTmp[r2] += 1
    return count


if __name__ == '__main__':
    print(countKDifference([3, 2, 1, 5, 4], 2))