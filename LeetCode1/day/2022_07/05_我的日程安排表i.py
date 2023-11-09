class MyCalendar:

    def __init__(self):
        self.books = []
        self.keys = []

    def book(self, start: int, end: int) -> bool:
        import bisect
        i1 = bisect.bisect_left(self.keys, start)
        i2 = bisect.bisect_left(self.keys, end)
        # print(i1, i2, start, end, self.skill, self.keys)
        if i1 != i2:
            return False
        if i1 == 0:
            if len(self.books) and self.books[0][0] == end:
                self.books[0][0] = start
                self.keys[0] = start
                return True
            elif len(self.books) and self.books[0][0] < end:
                return False
            else:
                self.books = [[start, end]] + self.books
                self.keys = [start] + self.keys
                return True
        if i1 == len(self.books):
            if self.books[-1][-1] > start:
                return False
            if self.books[-1][-1] == start:
                self.books[-1][-1] = end
                return True
            self.books = self.books + [[start, end]]
            self.keys.append(start)
            return True
        # print(self.skill, i1)
        l, r = self.books[i1 - 1][-1], self.books[i1][0]
        l1, r1 = self.books[i1 - 1][0], self.books[i1][-1]
        if l > start or r < end:
            return False

        if l == start:
            if r == end:
                self.books = self.books[:i1 - 1] + [[l1, r1]] + self.books[i1 + 1:]
                self.keys = self.keys[:i1 - 1] + [l1] + self.keys[i1 + 1:]
            else:
                self.books[i1 - 1][1] = end
        else:
            if r == end:
                self.books[i1][0] = start
                self.keys[i1] = start
            else:
                self.books = self.books[:i1] + [[start, end]] + self.books[i1:]
                self.keys = self.keys[:i1] + [start] + self.keys[i1:]

        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.LeetCode1(start,end)