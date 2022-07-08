class Solution:
    def reverse(self, x: int) -> int:
        reversed_num = 0
        z = 0

        if(x >= 0):
            while x != 0:
                digit = x % 10
                reversed_num = reversed_num * 10 + digit
                x //= 10

        else:
            x = x*(-1)
            while x != 0:
                digit = x % 10
                reversed_num = reversed_num * 10 + digit
                x //= 10
            reversed_num = reversed_num * (-1)
        if reversed_num < (-2**31) or reversed_num > (2**31)-1:
            return 0
        return reversed_num
