class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            t = n
            check = []
            while t > 0:
                check.append(t % i)
                t = t // i
            if check != check[::-1]:
                return False
        return True


# class Solution:
#   def isStrictlyPalindromic(self, n: int) -> bool:
#      pass #return False
