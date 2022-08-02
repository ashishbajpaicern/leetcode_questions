class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        l = []
        for i in nums:
            if i not in l:
                l.append(i)
        l.sort()
        if len(l) < 3:
            return l[-1]
        else:
            return l[-3]
