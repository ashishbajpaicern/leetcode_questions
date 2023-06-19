class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        while True:
            new = []
            for i in range(len(nums) - 1):
                new.append((nums[i] + nums[i + 1]) % 10)
            if len(new) == 1:
                return new[0]
            else:
                nums = new
