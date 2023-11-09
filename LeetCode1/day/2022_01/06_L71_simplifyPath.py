from unittest import TestCase

# 简化路径
"""
给你一个字符串 path ，表示指向某一文件或目录的Unix 风格 绝对路径 （以 '/' 开头），请你将其转化为更加简洁的规范路径。

在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..）表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。任意多个连续的斜杠（即，'//'）都被视为单个斜杠 '/' 。 对于此问题，任何其他格式的点（例如，'...'）均被视为文件/目录名称。

请注意，返回的 规范路径 必须遵循下述格式：

始终以斜杠 '/' 开头。
两个目录名之间必须只有一个斜杠 '/' 。
最后一个目录名（如果存在）不能 以 '/' 结尾。
此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 '.' 或 '..'）。
返回简化后得到的 规范路径 。
"""
# 解题思路


def simplifyPath(path: str) -> str:
    """
    按/分割成列表后分析，去除.和''， 将..解析。拼接成字符串。 也可用栈来做。
    :param path:
    :return:
    """
    lDir = path.split('/')
    lResDir = []
    for sDir in lDir:
        if not sDir:  # 空格
            continue
        if sDir == '..':
            lResDir = lResDir[:-1]
            continue
        if sDir == '.':
            continue
        lResDir.append(sDir)
    return '/' + '/'.join(lResDir)

    # # 方案二栈
    # stack = []
    # lResDir = []
    # for s in path:
    #     if s == '/':
    #         sDir = str(''.join(stack))
    #         stack = []
    #         if not sDir or sDir == '.':
    #             continue
    #         if sDir == '..':
    #             lResDir = lResDir[:-1]
    #             continue
    #         lResDir.append(sDir)
    #         continue
    #     stack.append(s)
    # if stack:
    #     sDir = str(''.join(stack))
    #     stack = []
    #     if not sDir or sDir == '.':
    #         pass
    #     if sDir == '..':
    #         lResDir = lResDir[:-1]
    #         pass
    #     lResDir.append(sDir)
    # return '/' + '/'.join(lResDir)


class Test(TestCase):

    def test_1(self):
        self.assertEqual(simplifyPath('/home/'), '/home')

    def test_2(self):
        self.assertEqual(simplifyPath('../'), '/')

    def test_3(self):
        self.assertEqual(simplifyPath('/home//foo'), '/home/foo')

    def test_4(self):
        self.assertEqual(simplifyPath('/a/../../b/../c//.//'), '/c')

    def test_5(self):
        self.assertEqual(simplifyPath('/a/./b/../../c/'), '/c')
