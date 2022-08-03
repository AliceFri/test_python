import re
from typing import List


class Solution:

    def diffWaysToCompute(self, expression: str) -> List[int]:
        # print(expression)
        if not expression:
            return []
        ret = []
        chrInd = []
        for ind, c in enumerate(expression):
            if c in '+-*':
                chrInd.append(ind)
        # print(chrInd)
        if not chrInd:
            return [int(expression)]

        for i in chrInd:
            # print(expression, i, expression[0:i], expression[i+1:])
            l1 = self.diffWaysToCompute(expression[0:i])
            l2 = self.diffWaysToCompute(expression[i+1:])
            for a in l1:
                for b in l2:
                    if expression[i] == '+':
                        ret.append(a + b)
                    elif expression[i] == '-':
                        ret.append(a - b)
                    else:
                        ret.append(a * b)


        return ret


