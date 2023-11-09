class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        grid = [[0] * n for _ in range(m)]

        def _cin(a, b):
            s = 0
            while a:
                s += (a % 10)
                a = a // 10
            while b:
                s += (b % 10)
                b = b // 10
            return s <= k

        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        stack = [(0, 0)]
        visited = set([(0, 0)])
        while stack:
            x, y = stack.pop()
            for ix, iy in move:
                nx, ny = x + ix, y + iy
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or (nx, ny) in visited or not _cin(nx, ny):
                    continue
                stack.append((nx, ny))
                visited.add((nx, ny))

        return len(visited)


if __name__ == '__main__':
    print(Solution().movingCount(1, 2, 1))