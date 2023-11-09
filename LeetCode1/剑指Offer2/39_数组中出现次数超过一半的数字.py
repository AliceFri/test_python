"""
Easy

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
"""
from typing import List

"""
思路:    1. 找中位数  partion
        2. 一次遍历 + 哈希表 ==> 打擂台的形式优化
        3. 排序 取中位数
        4. 计数法 ， 选定一个数， 刚好是他就 + 1， 不是就减一 count为0时换一个数。 最后得到的数即为答案
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        num = -1
        for i in nums:
            if count == 0:
                num = i
                count += 1
            elif num == i:
                count += 1
            else:
                count -= 1
        return num


if __name__ == '__main__':
    print(Solution().majorityElement([1, 1, 2]))