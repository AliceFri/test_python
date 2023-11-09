# Related Topics 广度优先搜索 数组 矩阵 👍 56 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def flipChess(self, chessboard) -> int:
        ans = 0
        for a in range(len(chessboard)):
            for b in range(len(chessboard[0])):
                if chessboard[a][b] != '.':
                    continue
                itmp = 0
                s = set([(a, b)])
                l = [(a, b)]
                while l:
                    a1, b1 = l.pop()
                    # 8 个方向都要试试
                    for mv in [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]:
                        a0, b0 = a1, b1
                        ltmp = []
                        close = False
                        while True:
                            a0 += mv[0]
                            b0 += mv[1]
                            if 0 <= a0 < len(chessboard) and 0 <= b0 < len(chessboard[0]):
                                if chessboard[a0][b0] == '.':
                                    break
                                if chessboard[a0][b0] == 'O':
                                    ltmp.append((a0, b0))
                                else:
                                    close = True
                                    break
                            else:
                                break
                        if close and ltmp:
                            for t in ltmp:
                                if t not in s:
                                    s.add(t)
                                    itmp += 1
                                    l.append(t)
                ans = max(ans, itmp)

        return ans

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().flipChess([".X.",".O.","XO."]))
