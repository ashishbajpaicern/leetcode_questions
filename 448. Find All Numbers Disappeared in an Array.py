class Solution(object):
    def findDisappearedNumbers(self, nums):
        a = []
        l = set(nums)
        for i in range(1, len(nums)+1):
            if i not in l:
                a.append(i)
        return a
