# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
import re


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if '[' not in s:
            return NestedInteger(int(s))

        first = NestedInteger()
        inputNestedStack = [first]
        l = re.split("([,\[\]])", s)
        # print(l)
        for key in l:
            if key == '':
                continue
            elif key == '[':
                new = NestedInteger()
                inputNestedStack[-1].add(new)
                inputNestedStack.append(new)
            elif key == ']':
                inputNestedStack.pop()
            elif key == ',':
                continue
            else:
                inputNestedStack[-1].add(NestedInteger(int(key)))

        return first.getList()[0]

