class Solution:
    def reformat(self, s: str) -> str:
        n, c = [], []

        for i in s:
            if ord(i) >= ord('0') and ord(i) - ord('0') <= 9:
                n.append(i)
            else:
                c.append(i)

        # print(n, c)
        i = abs(len(n) - len(c))
        if i >= 2:
            return ""

        s = []
        if len(n) >= len(c):
            for i in range(len(n) + len(c)):
                if i %2==0:
                    s.append(n[i//2])
                else:
                    s.append(c[i//2])
        else:
             for i in range(len(n) + len(c)):
                if i %2==0:
                    s.append(c[i//2])
                else:
                    s.append(n[i//2])
        return ''.join(s)