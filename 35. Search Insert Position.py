class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target not in nums:
            nums.append(target)
        nums.sort()
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            middle = (left + right) // 2
            if target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left = middle + 1
            else:
                return middle
