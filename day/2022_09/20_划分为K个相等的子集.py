"""
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
nums = [4, 3, 2, 3, 5, 2, 1], k = 4
"""
import collections
import functools
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True

        nums.sort()
        _sum = sum(nums)
        if _sum % k != 0:
            return False

        _s = _sum // k

        # has_solution = False
        # c = collections.defaultdict(int)
        @functools.cache
        def _dfs(dp, s):
            # c[(dp, s)] += 1
            # nonlocal has_solution
            if s == _sum:
                # has_solution = True
                return True
            for i in range(len(nums)):
                if nums[i] > _s or ((s % _s) + nums[i]) > _s:
                    break
                if (2**i) & dp:
                    continue
                s += nums[i]
                dp += 2**i
                if _dfs(dp, s):
                    return True
                s -= nums[i]
                dp -= 2**i
            return False

        ret = _dfs(0, 0)
        # print(_dfs.cache_info())
        return ret
        # return has_solution


def _cache(func):
    d = {}
    i = 0
    print('--------------- in ------------------')

    def _wrapper(*args, **kwargs):
        print('--------------- in2 ------------------')
        nonlocal i
        i += 1
        d[i] = 1
        print(i)
        print(d)
        return func(*args, **kwargs)

    print('--------------- out ------------------')
    return _wrapper


@_cache
def hello():
    print('hello world')


if __name__ == '__main__':
    hello()
    hello()
    hello()
    # print(Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
    # print(Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 9], 4))
    # print(
    #     Solution().canPartitionKSubsets(
    #         [
    #             724,
    #             3908,
    #             1444,
    #             522,
    #             325,
    #             322,
    #             1037,
    #             5508,
    #             1112,
    #             724,
    #             424,
    #             2017,
    #             1227,
    #             6655,
    #             5576,
    #             543,
    #         ],
    #         4,
    #     )
    # )
