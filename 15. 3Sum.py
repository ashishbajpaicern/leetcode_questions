class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            target = -nums[i]
            start = i+1
            end = len(nums)-1
            while(start < end):
                summ = nums[start]+nums[end]
                if summ < target:
                    start += 1
                elif summ > target:
                    end -= 1
                else:
                    ans.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1
        return ans
