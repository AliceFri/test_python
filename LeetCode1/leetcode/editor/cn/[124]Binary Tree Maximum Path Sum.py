# A path in a binary tree is a sequence of nodes where each pair of adjacent 
# nodes in the sequence has an edge connecting them. A node can only appear in the 
# sequence at most once. Note that the path does not need to pass through the root. 
# 
# 
#  The path sum of a path is the sum of the node's values in the path. 
# 
#  Given the root of a binary tree, return the maximum path sum of any non-
# empty path. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# 
#  
# 
#  Example 2: 
# 
#  
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 
# = 42.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 3 * 10⁴]. 
#  -1000 <= Node.val <= 1000 
#  
#  Related Topics 树 深度优先搜索 动态规划 二叉树 👍 1801 👎 0

from typing import Optional

from LeetCode1.剑指Offer2 import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 返回 最大路径和， 包含该点的最大单条路径和
        def dfs(r):
            if not r:
                return -1001, -1001
            l1, l2 = dfs(r.left)
            r1, r2 = dfs(r.right)
            return max(l1, r1, r.val + max(l2, 0) + max(r2, 0)), max(l2, r2, 0) + r.val

        return dfs(root)[0]
# leetcode submit region end(Prohibit modification and deletion)
