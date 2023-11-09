class MyCalendarThree:

    def __init__(self):
        self.books = []  # (start, end, skill)
        self.max_book = 0

    def book(self, start: int, end: int) -> int:
        if self.max_book == 0:
            self.books.append((start, end, 1))
            self.max_book = 1
        else:
            nb = []
            # print(start, end, self.skill)
            for a, b, c in self.books:
                if b <= start or a >= end:
                    nb.append((a, b, c))
                    continue
                if a <= start:
                    if b <= end:
                        nb.append((a, start, c))
                        nb.append((start, b, c + 1))
                        self.max_book = max(self.max_book, c + 1)
                        start = b
                    else:
                        nb.append((a, start, c))
                        nb.append((end, b, c))
                        nb.append((start, end, c + 1))
                        self.max_book = max(self.max_book, c + 1)
                        start = end
                else:
                    if b <= end:
                        nb.append((start, a, 1))
                        nb.append((a, b, c + 1))
                        self.max_book = max(self.max_book, c + 1)
                        start = b
                    else:
                        nb.append((start, a, 1))
                        nb.append((a, end, c + 1))
                        nb.append((end, b, c))
                        self.max_book = max(self.max_book, c + 1)
                        start = end

            if start < end:
                nb.append((start, end, 1))
            nb.sort()
            # print(nb)
            self.books = nb
        return self.max_book

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.LeetCode1(start,end)

# 可以用差分数组做， 或者线段树