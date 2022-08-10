class Solution:
    def solveEquation(self, equation: str) -> str:
        # 1. 分割 =
        lis = equation.split("=")
        l, r = lis[0], lis[1]

        def parse(s):
            a, b = 0, 0
            p = ""
            fh = True  # true + , false -
            for c in s:
                if c == "x":
                    tmp = 1 if p == "" else int(p)
                    if not fh:
                        tmp = -tmp
                    a += tmp
                    p = ""
                    fh = True
                elif c in ("+", "-"):
                    if p:
                        tmp = int(p) if fh else -int(p)
                        b += tmp
                    p = ""
                    fh = True if c == "+" else False
                else:
                    p += c

            if p:
                tmp = int(p) if fh else -int(p)
                b += tmp

            return a, b

        a1, b1 = parse(l)
        a2, b2 = parse(r)
        a = a1 - a2
        b = b2 - b1
        if a == 0:
            if b != 0:
                return "No solution"
            return "Infinite solutions"
        return f"x={b//a}"


if __name__ == "__main__":
    print(Solution().solveEquation("x+5-3+x=6+x-2"))
    print(Solution().solveEquation("x=x"))
    print(Solution().solveEquation("2x=x"))
