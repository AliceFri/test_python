# 给你一个整数数组 nums，将 nums 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。 
# 
#  返回满足此条件的 任一数组 作为答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [3,1,2,4]
# 输出：[2,4,3,1]
# 解释：[4,2,3,1]、[2,4,1,3] 和 [4,2,1,3] 也会被视作正确答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5000 
#  0 <= nums[i] <= 5000 
#  
#  Related Topics 数组 双指针 排序 👍 264 👎 0

# 双指针法， 交换位置
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        iLow, iHigh = 0 , len(nums) - 1
        while iLow < iHigh:
            while iLow < iHigh and nums[iLow] % 2 == 0:
                iLow += 1
            while iLow < iHigh and nums[iHigh] % 2 == 1:
                iHigh -= 1
            if iLow < iHigh:
                nums[iLow], nums[iHigh] = nums[iHigh], nums[iLow]

        return nums
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().sortArrayByParity([3,1,2,4]))