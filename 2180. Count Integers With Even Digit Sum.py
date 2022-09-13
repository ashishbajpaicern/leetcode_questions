class Solution:
    def countEven(self, num: int) -> int:
        counter = 0
        for i in range(1, num+1):
            sum = 0
            while i > 0:
                temp = i % 10
                sum = sum + temp
                i = i // 10
            if sum % 2 == 0:
                counter = counter + 1
            else:
                continue
        return counter
