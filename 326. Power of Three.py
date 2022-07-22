class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 1:
            if n == 1:
                return True
            n = n / 3
        return False
