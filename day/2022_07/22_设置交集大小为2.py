from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: (x[0], -x[1]))

        # print(intervals)
        ans = []

        for l in intervals[::-1]:
            i0, i1 = l[0], l[1]
            # print(i0, i1, ans)

            if len(ans) >= 2 and i1 >= ans[-2]:
                continue

            if len(ans) >= 1 and ans[-1] >= i0 and ans[-1] <= i1:
                ans.append(i0)

            else:
                ans.append(i0 + 1)
                ans.append(i0)

        return len(ans)



