class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            new = []
            for j in res:
                new.append(j + [i])

            res.extend(new)
        n = []
        for i in res:
            i.sort()
        for i in res:
            if i not in n:
                n.append(i)
        return n
