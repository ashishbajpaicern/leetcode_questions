class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        a = []
        counter = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                a.append(matrix[i][j])
        a.sort()
        return (a[k-1])
