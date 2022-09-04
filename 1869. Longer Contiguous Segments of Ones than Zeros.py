class Solution:
    def checkZeroOnes(self, s: str) -> bool:

        res0 = 0
        res1 = 0

        count0 = 0
        count1 = 0

        for i in s:
            if i == '1':
                count1 += 1
                res1 = max(res1, count1)
                count0 = 0

            else:
                count0 += 1
                res0 = max(res0, count0)
                count1 = 0
        return res0 < res1
