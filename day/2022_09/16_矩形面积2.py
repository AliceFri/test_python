from typing import List


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        hbound = set()
        for rect in rectangles:
            # 下边界
            hbound.add(rect[1])
            # 上边界
            hbound.add(rect[3])

        hbound = sorted(hbound)
        m = len(hbound)
        # 「思路与算法部分」的 length 数组并不需要显式地存储下来
        # length[i] 可以通过 hbound[i+1] - hbound[i] 得到
        seg = [0] * (m - 1)

        sweep = list()
        for i, rect in enumerate(rectangles):
            # 左边界
            sweep.append((rect[0], i, 1))
            # 右边界
            sweep.append((rect[2], i, -1))
        sweep.sort()

        ans = i = 0
        while i < len(sweep):
            j = i
            while j + 1 < len(sweep) and sweep[i][0] == sweep[j + 1][0]:
                j += 1
            if j + 1 == len(sweep):
                break

            # 一次性地处理掉一批横坐标相同的左右边界
            for k in range(i, j + 1):
                _, idx, diff = sweep[k]
                left, right = rectangles[idx][1], rectangles[idx][3]
                for x in range(m - 1):
                    if left <= hbound[x] and hbound[x + 1] <= right:
                        seg[x] += diff

            cover = 0
            for k in range(m - 1):
                if seg[k] > 0:
                    cover += hbound[k + 1] - hbound[k]
            ans += cover * (sweep[j + 1][0] - sweep[j][0])
            i = j + 1

        return ans % (10**9 + 7)


class Solution1:
    def rectangleArea(self, rs: List[List[int]]) -> int:
        ps = []
        for info in rs:
            ps.append(info[0])
            ps.append(info[2])
        ps.sort()
        ans = 0
        for i in range(1, len(ps)):
            a, b = ps[i - 1], ps[i]
            width = b - a
            if width == 0:
                continue
            lines = [(info[1], info[3]) for info in rs if info[0] <= a and b <= info[2]]
            lines.sort()
            height, l, r = 0, -1, -1
            for cur in lines:
                if cur[0] > r:
                    height += r - l
                    l, r = cur
                elif cur[1] > r:
                    r = cur[1]
            height += r - l
            ans += height * width
        return ans % 1000000007


if __name__ == '__main__':
    print(Solution1().rectangleArea([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]))
