class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        previous = []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        new = []
        for i in range(numRows-2):
            previous = res[-1]
            new.append(1)
            for j in range(len(previous)-1):
                new.append(previous[j]+previous[j+1])
            new.append(1)
            res.append(new)
            new = []
        return (res)
