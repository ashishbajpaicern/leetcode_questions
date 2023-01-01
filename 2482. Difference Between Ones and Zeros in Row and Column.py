class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        row1 = [0]*m
        row0 = [0]*m
        col1 = [0]*n
        col0 = [0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    row0[i] = row0[i] + 1
                    col0[j] = col0[j] + 1
                else:
                    row1[i] = row1[i] + 1
                    col1[j] = col1[j] + 1
        for i in range(m):
            for j in range(n):
                grid[i][j] = row1[i] + col1[j] - row0[i] - col0[j]
        return grid

        print(row0)
        print(col0)
        print(row1)
        print(col1)
