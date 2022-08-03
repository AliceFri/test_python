class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        def GetNextNum(n1):
            if n1 * 10 <= n:
                return n1 * 10

            if n1 % 10 == 9 and (n1 + 1) <= n:
                n1 += 1
                while n1 % 10 == 0:
                    n1 = n1 // 10
                return n1

            if n1 + 1 <= n:
                return n1 + 1

            n2 = n1 // 10 + 1
            while n2 % 10 == 0:
                n2 = n2 // 10
            return n2

        l = [1]
        for i in range(n - 1):
            iNew = GetNextNum(l[-1])
            l.append(iNew)

        return l