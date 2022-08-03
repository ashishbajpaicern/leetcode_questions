class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for item in set(nums):   # iterating over unique elements with set
            if nums.count(item) > len(nums) // 2:
                return item
