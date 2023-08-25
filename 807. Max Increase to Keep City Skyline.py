class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax = []
        colMax = []
        res = 0
        for i in range(len(grid)):
            m1 = 0
            m2 = 0
            for j in range(len(grid)):
                if m1 < grid[i][j]:
                    m1 = grid[i][j]
                if m2 < grid[j][i]:
                    m2 = grid[j][i]

            rowMax.append(m1)
            colMax.append(m2)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] < min(rowMax[i], colMax[j]):
                    res = res + -1 * grid[i][j] + min(rowMax[i], colMax[j])
        return res
