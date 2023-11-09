from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n, ans = len(arr), 0
        l, r = [-1] * n, [n] * n
        stk = []
        for i in range(n):
            while stk and arr[stk[-1]] >= arr[i]:
                r[stk.pop()] = i
            stk.append(i)
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and arr[stk[-1]] > arr[i]:
                l[stk.pop()] = i
            stk.append(i)
        print(l, r)
        for i in range(n):
            a, b = i - l[i], r[i] - i
            ans += a * b * arr[i]
        return ans % (10 ** 9 + 7)


if __name__ == '__main__':
    print(Solution().sumSubarrayMins([1, 2, 3, 4, 5]))