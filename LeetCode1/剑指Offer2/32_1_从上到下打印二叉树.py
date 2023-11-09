"""
中等

从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
"""
from typing import List

from LeetCode1.剑指Offer2 import TreeNode, t1


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        """
        可用 双端队列collections.deque 优化
        """
        res = []
        stack = [root]
        while stack:
            nstack = []
            for i in stack:
                if i is None:
                    continue
                else:
                    res.append(i.val)
                    nstack.append(i.left)
                    nstack.append(i.right)
            stack = nstack

        return res


if __name__ == '__main__':
    print(Solution().levelOrder(t1))
