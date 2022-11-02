from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # 1. 前缀和
        pre = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            pre[i + 1] = nums[i] + pre[i]

        # 2. 对前缀和 和可能用到的节点离散化
        s = set()
        for i in pre:
            s.add(i)
            s.add(i - lower)
            s.add(i - upper)

        l = sorted(list(s))
        s = {i: ind + 1 for ind, i in enumerate(l)}
        n = len(l)

        # 树状数组
        _nums = [0] * (n + 1)

        def _add(ind, iadd):
            while ind <= n:
                _nums[ind] += iadd
                ind += ind & (-ind)

        def _query(ind):
            cnt = 0
            while ind > 0:
                cnt += _nums[ind]
                ind -= ind & (-ind)
            return cnt

        total = 0
        for i in range(len(pre)):
            c = _query(s[pre[i] - lower]) - _query(s[pre[i] - upper] - 1)
            total += c
            _add(s[pre[i]], 1)

        return total


if __name__ == '__main__':
    print(Solution().countRangeSum([-2, 5, -1], -2, 2))
    print(Solution().countRangeSum([0], 0, 0))
