class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        nrows = len(mat)
        ncols = len(mat[0])
        output = 0
        for i in range(nrows):
            for j in range(ncols):
                if i == j or i+j == nrows-1:
                    output += mat[i][j]
        return output
