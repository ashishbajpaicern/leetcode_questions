class Solution:
    def arrangeCoins(self, n: int) -> int:
        counter = 0
        if n == 1:
            return 1
        for i in range(1, n):
            if n < i:
                break
            n = n - i
            counter = counter + 1
        return counter
