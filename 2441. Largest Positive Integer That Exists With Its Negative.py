class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        max = -1
        for i in nums:
            if i > 0 and ((-1)*i in nums):
                if i > max:
                    max = i
        return max
