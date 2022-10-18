class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num == 0:
            return True
        for i in range(num):
            i = str(i)
            rev = i[::-1]
            if int(i) + int(rev) == num:
                return True
        return False
