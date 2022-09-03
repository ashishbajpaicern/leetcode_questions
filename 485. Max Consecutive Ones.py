class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter = counter + 1
            elif nums[i] == 0:
                res = max(res, counter)
                counter = 0
        if counter > res:
            return counter
        return res
