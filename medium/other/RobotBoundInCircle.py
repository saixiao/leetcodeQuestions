class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        on_right = {
            "U": "R",
            "R": "D",
            "D": "L",
            "L": "U"
        }
        on_left = dict((v,k) for k,v in on_right.items())
        coord = [0,0]
        curr_D = "U"
        for instruction in list(instructions):
            if instruction == "R":
                curr_D = on_right[curr_D]
            elif instruction == "L":
                curr_D = on_left[curr_D]
            elif instruction == "G":
                coord = self.move(coord, curr_D)
        
        
        if coord == [0,0] or curr_D != "U":
            return True
        return False
         
        
    def move(self, coord, direction):
        offset = {
            "U": [0,1],
            "R": [1,0],
            "D": [0,-1],
            "L": [-1,0]
        }
        
        return [coord[0] + offset[direction][0], coord[1] + offset[direction][1]]