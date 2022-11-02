from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = [0] * (len(nums) + 1)
        for i, k in enumerate(nums):
            self.add(i + 1, k)

    def low_bit(self, n):
        return n & -n

    def query(self, n):     # 前 n 位的和
        cnt = 0
        while 0 < n < len(self.n):
            cnt += self.n[n]
            n -= self.low_bit(n)
        return cnt

    def add(self, n, iadd):
        while 0 < n < len(self.n):
            self.n[n] += iadd
            n += self.low_bit(n)

    def update(self, index: int, val: int) -> None:
        ipure = self.query(index + 1) - self.query(index)
        iadd = val - ipure
        self.add(index + 1, iadd)

    def sumRange(self, left: int, right: int) -> int:
        return self.query(right + 1) - self.query(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

if __name__ == '__main__':
    obj = NumArray([1, 2, 3, 4])
    print(obj.sumRange(0, 3))
    obj.update(0, 10)
    print(obj.sumRange(0, 1))
    obj.update(1, 12)
    print(obj.sumRange(1, 1))
    print(obj.sumRange(0, 1))