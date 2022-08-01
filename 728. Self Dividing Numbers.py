class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            j = i
            f = True
            while j > 0:
                if j % 10 == 0:
                    f = False
                    break
                if i % (j % 10) == 0:
                    j = j//10
                else:
                    f = False
                    break
            if f:
                ans.append(i)
        return ans
