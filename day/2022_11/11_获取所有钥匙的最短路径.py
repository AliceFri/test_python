# grid = ["@.a.#","###.#","b.A.B"]  8
from typing import List
from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        key_ids = {}
        ind = 0
        sx, sy = 0, 0
        has_start = 0
        q = deque()
        visited = {}
        m, n = len(grid), len(grid[0])

        # 准备工作
        for a in range(m):
            for b in range(n):
                if grid[a][b] == '@':
                    has_start = 1
                    sx, sy = a, b
                elif grid[a][b] in ('a', 'b', 'c', 'd', 'e', 'f'):
                    if grid[a][b] not in key_ids:
                        key_ids[grid[a][b]] = ind
                        ind += 1

        all_keys_mask = 2 ** len(key_ids) - 1

        # bfs
        if has_start:
            q.append((sx, sy, 0))
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited[(sx, sy, 0)] = 0
        while q:
            x, y, mask = q.popleft()
            for ax, ay in moves:
                nx, ny = x + ax, y + ay
                if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] == '#':
                    continue
                if grid[nx][ny] in ('A', 'B', 'C', 'D', 'E', 'F'):
                    k = key_ids[grid[nx][ny].lower()]
                    if not (mask >> k & 1):  # 没有钥匙
                        continue
                    if (nx, ny, mask) not in visited:
                        visited[(nx, ny, mask)] = visited[(x, y, mask)] + 1
                        q.append((nx, ny, mask))
                elif grid[nx][ny] in ('.', '@'):
                    if (nx, ny, mask) not in visited:
                        visited[(nx, ny, mask)] = visited[(x, y, mask)] + 1
                        q.append((nx, ny, mask))
                else:
                    nmask = mask | (2 ** key_ids[grid[nx][ny]])
                    if nmask == all_keys_mask:
                        return visited[(x, y, mask)] + 1
                    if (nx, ny, nmask) not in visited:
                        visited[(nx, ny, nmask)] = visited[(x, y, mask)] + 1
                        q.append((nx, ny, nmask))

        return -1


if __name__ == '__main__':
    print(Solution().shortestPathAllKeys(["@.a.#", "###.#", "b.A.B"]))
    print(Solution().shortestPathAllKeys(["@..aA", "..B#.", "....b"]))
    print(Solution().shortestPathAllKeys(["@.#aA"]))
