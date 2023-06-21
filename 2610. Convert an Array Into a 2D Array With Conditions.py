class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        check = []
        res = []
        flag = 0
        while True:
            check = []
            for key in d:
                if d[key] > 0:
                    flag = 1
                    check.append(key)
                    d[key] -= 1

            if flag == 0:
                break
            res.append(check)
            flag = 0

        return res
