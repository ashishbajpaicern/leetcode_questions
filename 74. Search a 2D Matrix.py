class Solution:
    def bsearch(self, l, r, target, mat):
        if l-r == 0:
            return False
        mid = (l+r)//2
        if mat[mid] == target:
            return True
        if target < mat[mid]:
            return self.bsearch(l, mid, target, mat)
        else:
            return self.bsearch(mid+1, r, target, mat)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = []
        for i in range(len(matrix)):
            a = matrix[i]
            l = 0
            r = len(matrix[0])
            check = self.bsearch(l, r, target, a)
            if check == True:
                break
        return check
