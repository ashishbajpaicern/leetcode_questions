class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:          
            cur = []            
            for c in res:       
                cur += [c + [n]]
            res += cur
        return res
        