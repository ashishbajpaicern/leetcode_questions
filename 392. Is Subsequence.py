class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for i in range(len(t)):
            if j == len(s):
                break
            if t[i] == s[j]:
                j = j + 1
        if j == len(s):
            return True
        else:
            return False
