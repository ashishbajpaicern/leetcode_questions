from itertools import permutations


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        a = []
        res = list(permutations(nums))
        for i in res:
            if i not in a:
                a.append(i)
        return a
