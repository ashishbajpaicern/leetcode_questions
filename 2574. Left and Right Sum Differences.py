class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lc = 0
        rc = sum(nums)
        res = []
        l = len(nums) - 1
        for i in range(len(nums)):
            rc -= nums[i]
            res.append(abs(lc - rc))
            lc += nums[i]

        return res
