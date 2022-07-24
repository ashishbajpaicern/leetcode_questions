class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = list(s)
        b = list(t)
        for i in a:
            if i in b:
                b.remove(i)
        return (b[0])
