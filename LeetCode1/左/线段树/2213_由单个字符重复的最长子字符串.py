# s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]

# 1 <= s.length <= 105
from typing import List

class Node:

    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.val = 0
        self.left = None
        self.right = None

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        # 算出初始值
        dp = [-1] * len(s)
