class Solution:
    def maxPower(self, s: str) -> int:
        a = 1
        b = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                a += 1
                b = max(b, a)
            else:
                b = max(b, a)
                a = 1
                pass

        return b
