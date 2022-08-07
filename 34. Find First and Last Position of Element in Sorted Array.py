class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i in range(len(nums)):
            if nums[i] > target:
                break
            if nums[i] == target:
                a.append(i)
        if a == []:
            return ([-1, -1])
        elif len(a) == 1:
            return ([a[0], a[0]])
        elif len(a) > 2:
            return ([a[0], a[-1]])
        return (a)
