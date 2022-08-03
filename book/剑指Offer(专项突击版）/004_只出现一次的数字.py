class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        set1, set2 = set(), set()

        for i in nums:
            if i not in set2:
                if i in set1:
                    set1.remove(i)
                    set2.add(i)
                else:
                    set1.add(i)

        return set1.pop()