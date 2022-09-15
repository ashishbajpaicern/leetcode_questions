class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = ''
        for i in s:
            nums += str(ord(i) - 96)

        while k > 0:
            sums = 0
            for j in nums:
                sums += int(j)
            nums = str(sums)
            k -= 1
        return sums
