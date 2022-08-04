class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        ret = True
        bin = list(format(n, "b"))
        for i in range(0, len(bin)-1):
            if bin[i] == bin[i+1]:
                ret = False
                break
            else:
                continue
        return ret
