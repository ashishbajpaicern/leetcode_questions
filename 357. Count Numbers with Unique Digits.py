class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n:
            return 1
        ans, start = 10, 9
        for i in range(1, min(10, n)):
            start *= (10 - i)
            ans += start
        return ans
