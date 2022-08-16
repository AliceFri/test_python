from typing import List


class OrderedStream:
    def __init__(self, n: int):
        self.words = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.words[idKey - 1] = value
        ret = []
        while self.ptr < len(self.words) and self.words[self.ptr] is not None:
            ret.append(self.words[self.ptr])
            self.ptr += 1
        return ret


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
