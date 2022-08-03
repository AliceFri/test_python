class Solution:
  def removeElement(self, nums: list[int], val: int) -> int:
    # 快慢指针
    iS = 0
    for iQ in range(0, len(nums)):
        if nums[iQ] != val:
            nums[iQ], nums[iS] = nums[iS], nums[iQ]
            iS += 1
    return iS