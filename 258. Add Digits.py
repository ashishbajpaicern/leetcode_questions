class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        while num > 9:
            while True:

                sum = sum + num % 10
                num = num // 10
                if num == 0:
                    break
            num = sum
            sum = 0
        return num
