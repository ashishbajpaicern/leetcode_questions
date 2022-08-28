class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        close = nums[0]
        for r in range(1, len(nums)):
            if abs(nums[r]) < abs(close):
                close = nums[r]
            if abs(nums[r]) == abs(close) and nums[r] > 0:
                close = nums[r]
        return close
