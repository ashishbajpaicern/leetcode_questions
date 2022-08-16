class Solution:
    def bsearch(self, l, r, target, nums):
        if l - r == 0:
            return -1
        mid = (l+r)//2

        if (target == nums[mid]):
            return mid
        if (target < nums[mid]):
            return self.bsearch(l, mid, target, nums)
        else:
            return self.bsearch(mid+1, r, target, nums)

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        res = self.bsearch(l, r, target, nums)
        return (res)
