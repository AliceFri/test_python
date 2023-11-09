"""
Mid

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。
例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

"""
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 双指针
        a, b = 0, 0
        stack = []
        while a < len(pushed):
            if pushed[a] == popped[b]:
                a += 1
                b += 1
            elif stack and stack[-1] == popped[b]:
                stack.pop(-1)
                b += 1
            else:
                stack.append(pushed[a])
                a += 1

        while b < len(popped):
            if popped[b] != stack.pop(-1):
                return False
            b += 1

        return True


if __name__ == '__main__':
    print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 2, 1]))