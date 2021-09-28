class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i != 0 and j != 0:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                        res += dp[i][j]
                    else:
                        dp[i][j] = 1
                        res += 1
                else:
                    dp[i][j] = 0
        
        return res