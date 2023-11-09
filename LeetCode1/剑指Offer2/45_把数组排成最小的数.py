"""
Mid

输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
"""
from typing import List
from functools import cmp_to_key
"""
若拼接字符串 x + y > y + xx+y>y+x ，则 xx “大于” yy ；
反之，若 x + y < y + xx+y<y+x ，则 xx “小于” yy ；
"""
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def _cmp(a1, a2):
            a1, a2 = str(a1), str(a2)
            if len(a1) < len(a2):
                return -_cmp(a2, a1)
            if not a1 and not a2:
                return 0
            if not a2:
                return 1
            for i in range(len(a1)):
                if i < len(a2):
                    if a1[i] > a2[i]:
                        return 1
                    if a1[i] < a2[i]:
                        return -1
                else:
                    return _cmp(a1[i:], a2)
                    # if pre is not None:
                        # if a1[i] > pre:
                            # return 1
                        # if a1[i] < pre:
                            # return -1
            return 0

        nums.sort(key=cmp_to_key(_cmp))
        nums = [str(i) for i in nums]

        return ''.join(nums)


if __name__ == '__main__':
    print(Solution().minNumber([824,938,1399,5607,6973,5703,9609,4398,8247]))