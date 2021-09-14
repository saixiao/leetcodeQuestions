class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        self.num_rows = len(matrix)
        self.num_cols = len(matrix[0])
        self.matrix = [[0 for y in range(self.num_cols + 1)] for x in range(self.num_rows + 1)]
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.matrix[i + 1][j + 1] = self.matrix[i][j+1] + self.matrix[i+1][j] + matrix[i][j] - self.matrix[i][j]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:      
        return self.matrix[row2 + 1][col2 + 1] - self.matrix[row2 + 1][col1] - self.matrix[row1][col2 + 1] + self.matrix[row1][col1]
