# 1、给定一个 int 类型的数组，表示一只股票最近 N 天的价格。假设你每次买卖只能一
# 股，可以买卖多次，但是手里最多只能持有一股。请写一个函数，计算你所能获取的最
# 大利润。
# 例如，一只股票最近 N 天的价格为 []int{1, 4, 2, 3}, 那么你所能获取的最大利润
# 为 4。
# Case 1
# 输入：prices = [1]
# 输出：0
# Case 2
# 输入: prices = [1, 4, 2, 3]
# 输出：4
# Case 3
# 输入：prices = [2, 100]
# 输出：98
# Case 4
# 输入：prices = [1, 5, 3, 9]
# 输出：10
def getProfit(prices: list):
    if len(prices) <= 1:
        return 0
    ans = 0
    dp = [[0, 0] for _ in range(len(prices))]   # [手里有股票的利润， 手里没有股票的利润]
    # 初始值
    dp[0] = [-prices[0], 0]
    for i in range(1, len(prices)):
        # dp的推理公式
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        ans = max(ans, dp[i][0], dp[i][1])
    return ans


# if __name__ == '__main__':
#     print(getProfit([1]))
#     print(getProfit([1, 4, 2, 3]))
#     print(getProfit([2, 100]))
#     print(getProfit([1, 5, 3, 9]))





# 2、将一个数组的所有元素向右移动若干单位，并把数组右侧溢出的元素填补在数组左侧的
# 空缺中，这种操作称为数组的循环平移。
# 给你一个不少于 2 个元素的数组 a，已知 a 是从一个升序且不包含重复元素的数组循
# 环平移 k (k 大于等于 0 且小于数组长度) 个单位而来。请写一个函数，输 入 int 类
# 型数组 a，返回 k 的值。
# 例如，对于数组 a = []int{5, 1, 2, 3, 4}，它由有序数组{1, 2, 3, 4, 5}循环平移
# 1个单位 而来，因此 k = 1。
# Case 1
# 输入：prices = [5, 1, 2, 3, 4]
# 输出：1
# Case 2
# 输入: prices = [4, 5, 6, 1, 2, 3]
# 输出：3
# Case 3
# 输入：prices = [7, 8, 9, 10, 2, 3, 4, 5, 6]
# 输出: 4
# Case 4
# 输入：prices = [10, 15, 20, 21, 35, 100, 101, 108, 1, 3, 9]
# 输出：8
# 1， 2， 3     ans = 0
# 3， 1， 2     ans = 1
# 2， 3， 1     ans = 2

def getK(nums):
    if nums[0] <= nums[-1]:
        return 0
    if nums[-1] < nums[0] and nums[-1] < nums[-2]:
        return len(nums) - 1
    # 这个值的特点是 小于其左边和右边的数, 如果不存在这样的数，答案就是 k - 1
    first, last = nums[0], nums[-1]
    ilow, ihigh = 0, len(nums) - 1

    while ilow <= ihigh:
        imid = ilow + ((ihigh - ilow) >> 1)
        # if imid == 0:
        #     # 这里不可能是答案，因为答案为0的情况第一行 已经return了
        #     ilow = imid + 1
        # elif imid == len(nums) - 1:
        #     ihigh = imid - 1
        if (nums[imid] < nums[imid - 1]) and (nums[imid] < nums[imid + 1]):
            return imid
        elif nums[imid] > first:
            ilow = imid + 1
        else:
            ihigh = imid - 1
    return len(nums) - 1

if __name__ == '__main__':
    print(getK([5, 1, 2, 3, 4]))
    print(getK([4, 5, 6, 1, 2, 3]))
    print(getK([7, 8, 9, 10, 2, 3, 4, 5, 6]))
    print(getK([10, 15, 20, 21, 35, 100, 101, 108, 1, 3, 9]))
