class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rev = arr[::-1]
        for i in range(len(rev)-1):
            if rev[i] > rev[i+1]:
                rev[i+1] = rev[i]
        rev = rev[::-1]
        rev.append(-1)
        return rev[1:]
