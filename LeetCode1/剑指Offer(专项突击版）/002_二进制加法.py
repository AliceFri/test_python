# 1. 两个栈相加 加入一个栈中

# 2. 转成int 相加后 转回 str

# 3. 补0对齐相加


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        stack1 = list(a)
        stack2 = list(b)
        # print(stack1, stack2)
        iFlag = 0
        stack = []
        while stack1 and stack2:
            i1, i2 = stack1.pop(), stack2.pop()
            i = int(i1) + int(i2) + iFlag
            if i == 1 or i == 3:
                stack.append('1')
            else:
                stack.append('0')
            if i >= 2:
                iFlag = 1
            else:
                iFlag = 0

        stack1 = stack1 if stack1 else stack2
        while stack1:
            i1 = stack1.pop()
            i = int(i1) + iFlag
            iFlag = 0
            if i == 0:
                stack.append('0')
            elif i == 1:
                stack.append('1')
            else:
                stack.append('0')
                iFlag = 1

        if iFlag:
            stack.append('1')

        return ''.join(stack[::-1])