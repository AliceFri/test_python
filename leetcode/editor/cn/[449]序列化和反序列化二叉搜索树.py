# 序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。 
# 
#  设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序
# 列化为最初的二叉搜索树。 
# 
#  编码的字符串应尽可能紧凑。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [2,1,3]
# 输出：[2,1,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数范围是 [0, 10⁴] 
#  0 <= Node.val <= 10⁴ 
#  题目数据 保证 输入的树是一棵二叉搜索树。 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 设计 二叉搜索树 字符串 二叉树 👍 304 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        return str(self.serialize1(root))

    def serialize1(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return []
        return [root.val, *self.serialize1(root.left), *self.serialize1(root.right)]
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data == '[]':
            return None
        l = data[1:-1].split(",")
        l1 = [int(v) for v in l]
        l2 = sorted(l1)

        return self.deserialize1(l1, l2)

    def deserialize1(self, l1, l2):
        if not l1:
            return None
        r = l1[0]
        ind = l2.index(r)

        t = TreeNode(r)
        left = self.deserialize1(l1[1: ind+1], l2[:ind])
        right = self.deserialize1(l1[ind+1:], l2[ind+1:])
        t.left = left
        t.right = right
        return t
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Codec().serialize([])
    print(Codec().deserialize(a))