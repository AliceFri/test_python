from unittest import TestCase

# 括号的最大嵌套深度


def maxDepth(s: str) -> int:
    """
    最大嵌套深度， 栈遍历， O(n); 可用一个计数器替代栈
    :param s:
    :return:
    """
    iDepth = 0
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            iDepth = max(iDepth, len(stack))
            stack.pop(-1)
    return iDepth


class Test(TestCase):

    def test_1(self):
        self.assertEqual(maxDepth("(1+(2*3)+((8)/4))+1"), 3)

    def test_2(self):
        self.assertEqual(maxDepth("(1)+((2))+(((3)))"), 3)

    def test_3(self):
        self.assertEqual(maxDepth("1+(2*3)/(2-1)"), 1)

    def test_3(self):
        self.assertEqual(maxDepth("1"), 0)