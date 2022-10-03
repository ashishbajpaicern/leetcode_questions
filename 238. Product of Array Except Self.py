class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        if nums.count(0) > 1:
            for i in range(len(nums)):
                nums[i] = 0
            return nums
        for i in nums:
            if i == 0:
                continue
            else:
                prod = prod * i

        if 0 in nums:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = prod
                else:
                    nums[i] = 0
            return nums
        for i in range(len(nums)):
            nums[i] = prod // nums[i]
        return nums
