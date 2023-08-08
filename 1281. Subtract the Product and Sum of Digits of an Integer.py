class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        p = 1
        while n > 0:
            tmp = n % 10
            n = n // 10
            p *= tmp
            s += tmp
        return p - s
