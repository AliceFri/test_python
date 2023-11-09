from collections import Counter
from math import gcd
from typing import List


class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort(key=lambda x: (x % 2, x))
        target.sort(key=lambda x: (x % 2, x))
        print(nums, target)
        # 前面的排序相当于对于奇数偶数进行了分类，前面为奇数，后面为偶数
        return sum(abs(x - y) for x, y in zip(nums, target)) // 4

    # 作者：小羊肖恩
    # 链接：https: // leetcode.cn / circle / discuss / uO4WuN / view / CUy95z /
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution3:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        tmp = sorted(list(zip(nums, cost)))
        tot, note = sum(cost), 0
        for num, c in tmp:
            note += c
            if note >= tot // 2:
                chosen = num
                break
        return sum(c * abs(num - chosen) for num, c in tmp)


class Solution2:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans, n = 0, len(nums)
        for l in range(n):
            tmp = nums[l]
            for r in range(l, n):
                tmp = gcd(tmp, nums[r])
                if tmp == k: ans += 1
                elif tmp % k: break
        return ans


if __name__ == "__main__":
    print(Solution().makeSimilar([8, 12, 6], [2, 14, 10]))
    print(Solution().makeSimilar([2, 4], [2, 4]))
    print(Solution().makeSimilar([4, 2], [2, 4]))

    print(Solution3().minCost([1, 3, 5, 2], [2, 3, 1, 14]))
