class RangeModule:

    def __init__(self):
        self.ranges = []


    def addRange(self, left: int, right: int) -> None:
        newrange = []
        mina, maxa = left, right
        for a, b in self.ranges:
            if b >= left and a <= right:
                mina = min(a, mina)
                maxa = max(b, maxa)
            else:
                newrange.append((a, b))
        newrange.append((mina, maxa))
        newrange.sort()
        self.ranges = newrange
        # print(self.ranges, left, right, "insert")


    def queryRange(self, left: int, right: int) -> bool:
        # print(self.ranges, left, right, "query")
        for a, b in self.ranges:
            if a <= left and b >= right:
                # print('true')
                return True
        # print('false')
        return False


    def removeRange(self, left: int, right: int) -> None:
        newrange = []
        for a, b in self.ranges:
            if a >= right or b <= left:
                newrange.append((a, b))
            else:
                if a >= left and b <= right:
                    continue
                elif a >= left and b > right:
                    newrange.append((right, b))
                elif a < left and b <= right:
                    newrange.append((a, left))
                else:
                    newrange.append((a, left))
                    newrange.append((right, b))
        newrange.sort()
        self.ranges = newrange
        # print(self.ranges, left, right, "remove")


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)