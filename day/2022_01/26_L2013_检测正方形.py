from collections import defaultdict


class DetectSquares:

    def __init__(self):
        self.m_X = defaultdict(dict)
        self.m_Y = defaultdict(dict)
        self.m_Points = []

    def add(self, point: list[int]) -> None:
        self.m_Points.append(point)
        x, y = point
        self.m_X[x].setdefault(y, 0)
        self.m_X[x][y] += 1
        self.m_Y[y].setdefault(x, 0)
        self.m_Y[y][x] += 1

    def count(self, point: list[int]) -> int:
        x, y = point
        iCnt = 0
        for i, num1 in self.m_X[x].items():
            if i == y or num1 == 0:
                continue
            iSide = abs(i - y)
            for p, num2 in self.m_Y[y].items():
                if p == x or abs(p - x) != iSide or num2 == 0:
                    continue
                if p in self.m_Y[i]:
                    iCnt = iCnt + self.m_Y[i][p] * num1 * num2
        return iCnt