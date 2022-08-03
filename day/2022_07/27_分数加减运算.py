class Solution:
    def fractionAddition(self, expression: str) -> str:

        lRet = []

        t = []
        for c in expression:
            if c in ('-', '+') and t:
                lRet.append(''.join(t))
                t = [c]
            else:
                t.append(c)
        if t:
            lRet.append(''.join(t))
        # print(lRet)

        lR = []
        for s in lRet:
            c1, c2, c3 = 0, 0, 0
            if s[0] == '-':
                c1 = 1
                s = s[1:]
            elif s[0] == '+':
                s = s[1:]

            t = s.split('/')
            c2 = int(t[0])
            if c1:
                c2 = -c2
            c3 = int(t[1])

            lR.append((c2, c3))
        # print(lR)

        father = 1
        for i in lR:
            father *= i[1]

        son = 0
        for i in lR:
            son = son + i[0] * (father // i[1])

        import math
        g = math.gcd(son, father)
        s = f'{son // g}/{father // g}'

        return s



