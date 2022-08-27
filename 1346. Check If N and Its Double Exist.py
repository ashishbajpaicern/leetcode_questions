class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        res = []
        for num in arr:
            if num*2 in res or num/2 in res:
                return True
            else:
                res.append(num)
        return False
