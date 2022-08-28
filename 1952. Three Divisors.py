class Solution:
    def isThree(self, n: int) -> bool:
        counter = 0
        for i in range(1, n+1):
            if n % i == 0:
                counter = counter + 1
        print(counter)
        if counter == 3:
            return True
        else:
            return False
