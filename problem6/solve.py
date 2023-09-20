class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = [''] * numRows
        row, jump = 0, 1
        if(numRows ==1): return s
        for char in s:
            result[row] += char
            if row == 0:
                jump = 1
            elif row == numRows - 1:
                jump = -1
            row += jump
        
        return ''.join(result)
