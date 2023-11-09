import collections


class Solution:
    def minSubArrayLen(self, target: int, nums: list) -> int:
        il, ir = 0, 0
        r = 10000

        for ir in range(0, len(nums)):
            iS = sum(nums[il:ir + 1])
            while iS >= target:
                r = min(r, ir -il + 1)
                iS -= nums[il]
                il += 1

        if r == 10000:
            return 0
        return r


# 904 水果成篮
class Solution1:
    def totalFruit(self, fruits: list) -> int:
        if len(fruits) <= 2:
            return len(fruits)

        il = 0
        lFruitType = {fruits[0]}
        iMax = 1
        for ih in range(1, len(fruits)):
            if fruits[ih] in lFruitType:
                iMax = max(iMax, ih - il + 1)
                continue
            elif len(lFruitType) < 2:
                lFruitType.add(fruits[ih])
                iMax = max(iMax, ih - il + 1)
                continue

            lFruitType = {fruits[ih], fruits[ih - 1]}
            for i in range(ih - 2, -1, -1):
                if fruits[i] == fruits[i + 1]:
                    continue
                il = i + 1
                break

        return iMax

    def minWindow(self, s: str, t: str) -> str:
        dT = collections.Counter(t)
        dS = collections.defaultdict(int)
        iDistance = 0

        iMin, iMinLeft, iMinRight = float('inf'), 0, 0

        iStart, iEnd = 0, 0
        # [iStart, iEnd]
        while iEnd < len(s):
            if s[iEnd] not in dT:
                iEnd += 1
                continue

            if dS[s[iEnd]] >= dT[s[iEnd]]:
                dS[s[iEnd]] += 1
                iEnd += 1
                continue
            dS[s[iEnd]] += 1
            iDistance += 1
            iEnd += 1

            while iDistance == len(t):
                if iMin >= iEnd - iStart:
                    iMin = iEnd - iStart
                    iMinLeft = iStart
                    iMinRight = iEnd - 1

                if s[iStart] not in dT:
                    iStart += 1
                    continue
                if dS[s[iStart]] > dT[s[iStart]]:
                    dS[s[iStart]] -= 1
                    iStart += 1
                    continue
                dS[s[iStart]] -= 1
                iDistance -= 1
                iStart += 1

        if iMin == float('inf'):
            return ''

        return s[iMinLeft: iMinRight + 1]


if __name__ == '__main__':
    print(Solution().minSubArrayLen(80, [10,5,13,4,8,4,5,11,14,9,16,10,20,8]))
    print(Solution1().totalFruit([1, 0, 1, 4, 1, 4, 1, 2, 3]))
    print(Solution1().minWindow("ADOBECODEBANC", 'ABC'))