from typing import List


# 用partion优化
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        import random
        def partion(l, r, t):
            i = random.randint(l, r)
            nums[i], nums[l] = nums[l], nums[i]

            low, high, p = l, r, l + 1  # 左边指示器， 右边指示器
            pl = nums[low]
            while p <= high:
                if nums[p] < pl:    # 换到左边去
                    nums[p], nums[low] = nums[low], nums[p]
                    low += 1
                    p += 1
                else:   # 换到右边去
                    nums[p], nums[high] = nums[high], nums[p]
                    high -= 1

            if low == t:
                return pl
            if low > t:
                return partion(l, low - 1, t)
            return partion(low + 1, r, t)

        t = partion(0, len(nums) - 1, (len(nums) - 1) // 2)
        # 三路partion
        ind = (len(nums) - 1) // 2
        i = 0
        k = ind - 1
        while i <= k:
            if nums[i] != t:
                i += 1
            else:
                nums[k], nums[i] = nums[i], nums[k]
                k -= 1
        i = len(nums) - 1
        k = ind + 1
        while i >= k:
            if nums[i] != t:
                i -= 1
            else:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1

        # nums.sort() 上面这些可以用这行代替， 时间复杂度从 O（n） -> O(nlgn)

        i, j = (len(nums) - 1) // 2, len(nums) - 1

        ret = nums[::]
        b = 0
        for k in range(len(nums)):
            b += 1
            if b % 2 == 1:
                nums[k] = ret[i]
                i -= 1
            else:
                nums[k] = ret[j]
                j -= 1

        # print(nums)
        return nums


if __name__ == '__main__':
    print(Solution().wiggleSort([1, 5, 10, 1, 6, 4, 2, 3]))