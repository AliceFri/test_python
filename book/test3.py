import bisect
from functools import cache


class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        z, fz = [], []
        for ind, c in enumerate(s):
            if c in ('2', '3', '5', '7'):
                z.append(ind)
            else:
                fz.append(ind)
        sz = set(z)
        sfz = set(fz)

        @cache
        def find(start, end, need_k):
            if start not in sz or end not in sfz:
                return 0
            if need_k == 1:
                if end - start + 1 >= minLength:
                    return 1
                return 0

            icnt = 0
            # k = bisect.bisect_right(z, start + minLength)
            for i in range(0, len(z)):
                if z[i] - 1 not in sfz:
                    continue
                if z[i] - start < minLength:
                    continue
                icnt += find(z[i], end, need_k - 1)
                # print(start, z[i], icnt)
                icnt = icnt % (10 ** 9 + 7)
            return icnt

        res = find(0, len(s) - 1, k)
        return res


if __name__ == '__main__':
    print(Solution().beautifulPartitions("23542185131", 3, 2))      # 3
    print(Solution().beautifulPartitions("2185131", 2, 2))       # 2
    print(Solution().beautifulPartitions("31", 1, 2))            # 1
    print(Solution().beautifulPartitions("5131", 2, 2))