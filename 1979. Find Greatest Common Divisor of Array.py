class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        max = 0
        for i in range(1, nums[-1]+1):
            if nums[0] % i == 0 and nums[-1] % i == 0:
                max = i
        if max == 0:
            return 1
        return max
