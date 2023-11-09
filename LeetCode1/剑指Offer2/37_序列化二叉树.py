"""

Hard
"""
from LeetCode1.剑指Offer2 import t1, TreeNode
"""
层遍历, 极端情况会超出时间限制

先序遍历  加上 #
"""

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ret = []
        stack = [root]
        while stack:
            l = []
            ns = []
            all_None = True
            for s in stack:
                if s:
                    l.append(s.val)
                    ns.append(s.left)
                    ns.append(s.right)
                    all_None = False
                else:
                    l.append(None)
                    ns.append(None)
                    ns.append(None)
            if all_None:
                return ret
            ret.append(l)
            stack = ns
        return ret[::]

    def deserialize(self, data):
        if not data or not data[0]:
            return None
        root = TreeNode(data[0][0])
        stack = [root]
        for ind in range(1, len(data)):
            ns = []
            d = data[ind]
            i = 0
            for s in stack:
                if not s:
                    i += 2
                    ns.append(None)
                    ns.append(None)
                    continue
                l, r = d[i], d[i + 1]
                i += 2
                if l is not None:
                    l = TreeNode(l)
                if r is not None:
                    r = TreeNode(r)
                s.left = l
                s.right = r
                ns.append(l)
                ns.append(r)
            stack = ns
        return root


if __name__ == '__main__':
    print(Codec().serialize(TreeNode(-1, TreeNode(0), TreeNode(1))))