from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        s = set(nums)
        for i in nums:
            s.add((i - 1) // 2)
        l = sorted(list(s))
        s = {i: ind + 1 for ind, i in enumerate(l)}
        n = len(l)

        _nums = [0] * (n + 1)

        def _add(ind, iadd):
            while ind <= n:
                _nums[ind] += iadd
                ind += ind & -ind

        def _query(ind):
            cnt = 0
            while ind > 0:
                cnt += _nums[ind]
                ind -= ind & -ind
            return cnt

        total = 0
        for i in range(len(nums) - 1, -1, -1):
            q = _query(s[(nums[i] - 1) // 2])
            total += q
            # print(q, total)
            _add(s[nums[i]], 1)

        return total


if __name__ == '__main__':
    print(Solution().reversePairs([1, 3, 2, 3, 1]))
    print(Solution().reversePairs([2, 4, 3, 5, 1]))