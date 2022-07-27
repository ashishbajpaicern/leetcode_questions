class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        for i in range(l - 1, 1, -1):
            if nums[i-2] + nums[i-1] > nums[i]:
                return nums[i-2] + nums[i-1] + nums[i]

        return 0
