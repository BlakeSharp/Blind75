class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        height,length = len(matrix), len(matrix[0])
        zcol,zrow = {}, {}
        for row in range(height):
            for col in range(length):
                if(matrix[row][col] == 0):
                    if(col not in zcol):
                        zcol[col] = True
                    if(row not in zrow):
                        zrow[row] = True

        for key in zcol:
            for item in range(height):
                matrix[item][key] = 0
        for key in zrow:
            for item in range(length):
                matrix[key][item] = 0
