class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        larger_nums = []
        for num in nums:
            larger_nums.append(sorted_nums.index(num))
        print(larger_nums)
        return larger_nums
