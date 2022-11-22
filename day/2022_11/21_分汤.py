from functools import cache


class Solution:
    def soupServings(self, n: int) -> float:
        @cache
        def _servings(n1, n2):
            r1 = 0
            for a, b in [(100, 0), (75, 25), (50, 50), (25, 75)]:
                a1, b1 = n1 - a, n2 - b
                if a1 <= 0 and b1 <= 0:
                    r1 += 0.125
                elif a1 <= 0 and b1 > 0:
                    r1 += 0.25
                elif b1 <= 0:
                    pass
                else:
                    r1 += 0.25 * _servings(a1, b1)
            return r1

        if n >= 10 ** 4:
            return 1
        return _servings(n, n)


if __name__ == '__main__':
    print(Solution().soupServings(10 ** 4))
    print(Solution().soupServings(660295675))
