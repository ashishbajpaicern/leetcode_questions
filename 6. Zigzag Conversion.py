class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        st = [""] * numRows
        row = 0
        flag = 0
        for i in s:
            st[row] = st[row] + i
            if row < numRows - 1 and flag == 0:
                row += 1
            elif row == numRows - 1 and flag == 0:
                flag = 1
                row -= 1
            elif row < numRows - 1 and flag == 1:
                row -= 1
            if row == 0:
                flag = 0
        return "".join(st)
