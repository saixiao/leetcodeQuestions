class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        # up, down, left, right
        validNextPaths = [None] * 7
        validNextPaths[1] = [{}, {}, {1,4,6}, {1,3,5}]
        validNextPaths[2] = [{2,3,4}, {2,5,6}, {}, {}]
        validNextPaths[3] = [{}, {2,5,6}, {1,4,6}, {}]
        validNextPaths[4] = [{}, {2,5,6}, {}, {1,3,5}]
        validNextPaths[5] = [{2,3,4}, {}, {1,4,6}, {}]
        validNextPaths[6] = [{2,3,4}, {}, {}, {1,3,5}]
        
        offsets = {
            0: [-1, 0],
            1: [1, 0],
            2: [0, -1],
            3: [0, 1]
        }
        
        enter_tile_thru_x = {
            1: {3: 3, 2: 2},
            2: {0: 0, 1: 1},
            3: {3: 1, 0: 2},
            4: {0: 3, 2: 1},
            5: {3: 0, 1: 2},
            6: {1: 3, 2: 0},
        }
        
        def walk_maze(x, y, grid, direction):
            visited = set()
            
            while True:           
                current_tile = grid[y][x]
                if y == m - 1 and x == n - 1:
                    return True

                offset = offsets[direction]
                valid_next_path = grid[y][x] 
                x = x + offset[1]
                y = y + offset[0]
                if 0 <= y < m and 0 <= x < n and str(x) + "," + str(y) not in visited:
                    if validNextPaths[current_tile][direction] != {} and grid[y][x] in validNextPaths[current_tile][direction]:
                        visited.add(str(x) + "," + str(y))
                        direction = enter_tile_thru_x[grid[y][x]][direction]
                        continue
                return False
        
        valid_direction =[i for i,v in enumerate(validNextPaths[grid[0][0]]) if v != {}]
        return walk_maze(0,0,grid,valid_direction[0]) or walk_maze(0,0,grid,valid_direction[1])
                        
            
            