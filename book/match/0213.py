class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        iCount = 0

        while num1 != 0 or num2 != 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            iCount += 1

        return iCount


if __name__ == '__main__':
    print(Solution().countOperations(2, 3))