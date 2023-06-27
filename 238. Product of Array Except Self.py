class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)
        mul = 1
        flag = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                flag = 1
                idx = i
            else:
                mul = mul * nums[i]
        if flag == 1:
            res = [0] * len(nums)
            res[idx] = mul
            return res
        for i in range(len(nums)):
            nums[i] = mul // nums[i]
        return nums
