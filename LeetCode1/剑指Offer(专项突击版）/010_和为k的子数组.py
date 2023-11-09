# 我用了 前缀和 + 哈希去做，勉强通过。。。
#


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        # 前缀和 + hash

        pre = [0] * len(nums)
        pre[0] = nums[0]

        dPre = {nums[0]: [0]}
        for i in range(1, len(nums)):
            pre[i] = nums[i] + pre[i - 1]
            if pre[i] not in dPre:
                dPre[pre[i]] = []
            dPre[pre[i]].append(i)
            # 可以在这里查找哈希，这样就不用去比较下面 的ii和i的大小问题。

        # print(pre, dPre)
        iRet = 0
        for i in range(len(nums)):
            if pre[i] == k:
                iRet += 1
            iFind = pre[i] - k
            # print('----', iFind, i)
            for ii in dPre.get(iFind, []):
                if ii < i:
                    iRet += 1
                else:
                    break

        return iRet

        # ret = pre_sum = 0
        # pre_dict = {0: 1}
        # for i in nums:
        #     pre_sum += i
        #     ret += pre_dict.get(pre_sum - k, 0)
        #     pre_dict[pre_sum] = pre_dict.get(pre_sum, 0) + 1
        # return ret

