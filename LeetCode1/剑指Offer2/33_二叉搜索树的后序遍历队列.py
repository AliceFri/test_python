"""
Mid

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果
"""
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        """左 右 根"""

        def _check(iStart, iEnd):
            if iEnd <= iStart:
                return True
            r = postorder[iEnd]

            ile = iStart
            while postorder[ile] < r:
                ile += 1

            for i in range(ile, iEnd):
                if postorder[i] < r:
                    return False
            # 左数组 iStart, ile -1
            # 右数组 ile, iEnd - 1
            return _check(iStart, ile - 1) and _check(ile, iEnd - 1)

        return _check(0, len(postorder) - 1)


if __name__ == '__main__':
    print(Solution().verifyPostorder([1, 6, 3, 2, 5]))
    print(Solution().verifyPostorder([1, 3, 2, 6, 5]))