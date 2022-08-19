"""
Mid

给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
"""
from collections import defaultdict
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 建立字典
        # d = defaultdict(list)
        # for a in range(len(board)):
        #     for b in range(len(board[0])):
        #         key = board[a][b]
        #         d[key].append((a, b))

        # if not d.get(word[0]):
        #     return False

        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        stack = []

        # for start in d.get(word[0]):
        #     used = {start}
        #     icheck = 1
        #     # 深度遍历
        #     stack.append((start, used, icheck))
        #     while stack:
        #         st, us, ic = stack.pop(-1)
        #         if ic >= len(word):
        #             return True
        #         check_world = word[ic]
        #         for im in move:
        #             nx, ny = st[0] + im[0], st[1] + im[1]
        #             if (
        #                 0 <= nx < len(board)
        #                 and 0 <= ny < len(board[0])
        #                 and board[nx][ny] == check_world
        #                 and (nx, ny) not in us
        #             ):
        #                 us1 = {t for t in us}
        #                 us1.add((nx, ny))
        #                 stack.append(((nx, ny), us1, ic + 1))

        # 回溯

        def check(start, icheck):
            if icheck >= len(word):
                return True
            for im in move:
                nx, ny = start[0] + im[0], start[1] + im[1]
                if (
                        0 <= nx < len(board)
                        and 0 <= ny < len(board[0])
                        and board[nx][ny] == word[icheck]
                        and (nx, ny) not in viseted
                ):
                    viseted.add((nx, ny))
                    if check((nx, ny), icheck + 1):
                        return True
                    viseted.remove((nx, ny))
            return False

        for a in range(len(board)):
            for b in range(len(board[0])):
                viseted = set([(a, b)])
                if board[a][b] == word[0] and check((a, b), 1):
                    return True

        return False


if __name__ == '__main__':
    # print(
    #     Solution().exist(
    #         [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
    #         "ABCCED",
    #     )
    # )
    print(
        Solution().exist(
            [["A", "A"]],
            "AAA",
        )
    )

    # A B C E
    # S F C S
    # A D E E
