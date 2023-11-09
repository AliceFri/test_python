"""
Easy

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )
"""

class CQueue:

    def __init__(self):
        # 列表只能使用append 和 pop(-1)
        self.stack1 = []    # 入栈
        self.stack2 = []    # 出栈
        self.size = 0

    def appendTail(self, value: int) -> None:
        self.size += 1
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.size == 0:
            return -1
        self.size -= 1
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop(-1))

        return self.stack2.pop(-1)


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()