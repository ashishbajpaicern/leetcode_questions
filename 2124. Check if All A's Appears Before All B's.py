class Solution:
    def checkString(self, s: str) -> bool:
        l = list(s)
        a = sorted(l)
        if a == l:
            return True
        else:
            return False
