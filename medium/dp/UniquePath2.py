class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1
        
        for y in range(len(obstacleGrid)):
            for x in range(len(obstacleGrid[0])):
                if x == 0 and y == 0:
                    continue

                if obstacleGrid[y][x] == 1:
                    obstacleGrid[y][x] = 0
                    continue
                    
                left = obstacleGrid[y][x - 1] if x > 0 else 0
                top = obstacleGrid[y - 1][x] if y > 0 else 0
        
                obstacleGrid[y][x] = left + top
        
        return obstacleGrid[-1][-1]