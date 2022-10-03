class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        previous = []
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        res = [[1], [1, 1]]
        new = []
        for i in range(rowIndex-1):
            previous = res[-1]
            new.append(1)
            for j in range(len(previous)-1):
                new.append(previous[j]+previous[j+1])
            new.append(1)
            res.append(new)
            new = []
        return (res[-1])
