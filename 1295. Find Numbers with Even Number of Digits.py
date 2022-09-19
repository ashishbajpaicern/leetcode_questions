class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even = 0
        for i in nums:
            counter = 0
            while i > 0:
                i = i // 10
                counter = counter + 1
            if counter % 2 == 0:
                even = even + 1
        return even
