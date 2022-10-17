class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        new = 0
        newarr = []
        for i in nums:
            new = 0
            while i > 0:
                tmp = i % 10
                new = new * 10 + tmp
                i = i//10
            newarr.append(new)
        nums.extend(newarr)
        numSet = set(nums)
        return len(numSet)
