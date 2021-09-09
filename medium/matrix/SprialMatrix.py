class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # return matrix and [*matrix.pop(0)] + self.spiralOrder(list(zip(*matrix))[::-1])
        next_move = {
            "r": "d",
            "d": "l",
            "l": "u",
            "u": "r"
        }
        
        offset = {
            "r": [0,1],
            "d": [1,0],
            "l": [0,-1],
            "u": [-1,0]
        }
        
        d = "r"
        res = []
        x = 0
        y = 0
        while True:
            if matrix[y][x] == "#":
                return res
            res.append(matrix[y][x])
            matrix[y][x] = "#"
            y_off = offset[d][0] 
            x_off = offset[d][1]
            # check bounds and #
            if 0 <= y_off + y < len(matrix) and 0 <=  x_off + x < len(matrix[0]): 
                if matrix[y_off + y][x_off + x] != "#":
                    y = y_off + y
                    x = x_off + x
                    continue
            d = next_move[d]
            y = offset[d][0] + y
            x = offset[d][1] + x

            if 0 > y or y > len(matrix) - 1 or 0 > x or x > len(matrix[0]) - 1: 
                return res
            
            
            
            
            