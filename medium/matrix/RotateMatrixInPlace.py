class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead., nxn
        """
        # transpose matrix
        for y in range(len(matrix)):
            for x in range(y):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
        
        # cw
        for i in range(len(matrix)):
            matrix[i].reverse()

        # ccw
        for i in range(ceil(len(matrix)/2)):
            matrix[i], matrix[-(i + 1)], = matrix[-(i + 1)], matrix[i]