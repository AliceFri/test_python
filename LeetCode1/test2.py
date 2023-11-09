import bisect


def is_increase(nums):
    l = len(nums)
    res = 0
    li = SortedList()
    for i in range(l):
        pre = bisect.bisect_left(li,nums[i])
        li.add(nums[i])
        res += (pre * (l-nums[i]-i+pre-1))
    return res


class Solution:
    def goodTriplets(self, nums1, nums2) -> int:
        if len(nums1)<3:return 0
        # nums1种的在nums2种的下标
        idx_of2 = [0]*len(nums2)
        for i,n in enumerate(nums2): idx_of2[n]=i
        idx_1in2 = [idx_of2[n] for n in nums1]
        # print(len(nums1),idx_1in2)
        return is_increase(idx_1in2)


if __name__ == '__main__':
    Solution().goodTriplets([4, 0, 1, 3, 2], [4, 1, 0, 2, 3])