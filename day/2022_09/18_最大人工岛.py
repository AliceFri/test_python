from typing import List

# 1 0 1
# 0 0 0
# 0 1 1


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # 先预处理
        x_max, y_max = len(grid), len(grid[0])
        move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ino = 0
        dpath = {}

        for x in range(x_max):
            for y in range(y_max):
                if grid[x][y] != 1:
                    continue
                path = set([(x, y)])
                stack = [(x, y)]
                while stack:
                    _x, _y = stack.pop()
                    for ix, iy in move:
                        nx, ny = _x + ix, _y + iy
                        if (
                            0 <= nx < x_max
                            and 0 <= ny < y_max
                            and grid[nx][ny] == 1
                            and (nx, ny) not in path
                        ):
                            path.add((nx, ny))
                            stack.append((nx, ny))
                _size = len(path)
                # print(path)
                for t in path:
                    _x, _y = t
                    grid[_x][_y] = _size
                    dpath[(_x, _y)] = (ino, _size)
                ino += 1

        # print(grid)
        # print(dpath)
        res = 1
        for x in range(x_max):
            for y in range(y_max):
                if grid[x][y] != 0:
                    continue

                nstack = []
                for ix, iy in move:
                    nx, ny = x + ix, y + iy
                    if 0 <= nx < x_max and 0 <= ny < y_max and grid[nx][ny]:
                        nstack.append(dpath.get((nx, ny)))

                _set = set()
                iadd = 0
                for t in nstack:
                    if t[0] not in _set:
                        iadd += t[1]
                        _set.add(t[0])

                res = max(res, iadd + 1)

        if res == 1 and grid[0][0]:
            return grid[0][0]
        return res

# class Solution:
#     def largestIsland(self, grid: List[List[int]]) -> int:
#         res = 1
#         dpath = set()
#         l_set = []
#         move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
#         x_max, y_max = len(grid), len(grid[0])
#
#         for x in range(x_max):
#             for y in range(y_max):
#                 # print(x, y)
#                 if grid[x][y] == 1:
#                     continue
#                 # print(x, y)
#
#                 stack = [(x, y)]
#                 path = set([(x, y)])
#
#                 # do
#                 nstack = []
#                 for ix, iy in move:
#                     nx, ny = x + ix, y + iy
#                     if (
#                         nx < 0
#                         or nx >= x_max
#                         or ny < 0
#                         or ny >= y_max
#                         or (nx, ny) in path
#                         or grid[nx][ny] == 0
#                     ):
#                         continue
#                     path.add((nx, ny))
#                     nstack.append((nx, ny))
#
#                 _should_ret = False
#                 for s in l_set:
#                     jump = False
#                     for t in nstack:
#                         if t not in s:
#                             jump = True
#                             break
#                     if not jump:
#                         _should_ret = True
#                         break
#
#                 if _should_ret or not nstack:
#                     continue
#
#                 while nstack:
#                     _x, _y = nstack.pop()
#                     for ix, iy in move:
#                         nx, ny = _x + ix, _y + iy
#                         if (
#                             nx < 0
#                             or nx >= x_max
#                             or ny < 0
#                             or ny >= y_max
#                             or (nx, ny) in path
#                             or grid[nx][ny] == 0
#                         ):
#                             continue
#                         path.add((nx, ny))
#                         nstack.append((nx, ny))
#                 # print(x, y, len(path))
#                 res = max(res, len(path))
#                 dpath = path
#                 l_set.append(path)
#
#         if not dpath and grid[0][0] == 1:
#             return x_max * y_max
#
#         return res


if __name__ == "__main__":
    print(Solution().largestIsland([[1, 0], [0, 1]]))
    print(Solution().largestIsland([[1, 1], [0, 1]]))
    print(Solution().largestIsland([[1, 1], [1, 1]]))
    print(Solution().largestIsland([[0, 0], [0, 1]]))
    print(Solution().largestIsland([[1, 0, 1], [0, 0, 0], [0, 1, 1]]))
