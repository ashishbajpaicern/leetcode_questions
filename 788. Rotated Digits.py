class Solution:
    def rotatedDigits(self, N: int) -> int:
        count = 0
        for x in range(1, N + 1):
            x = str(x)
            if "3" in x or "4" in x or "7" in x:
                continue
            if "2" in x or "5" in x or "6" in x or "9" in x:
                count += 1
        return count
