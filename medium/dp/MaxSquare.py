class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_side = 0
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0 for j in range(n)] for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i != 0 and j != 0:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                        max_side = max(max_side, dp[i][j])
                    else:
                        dp[i][j] = 1
                        max_side = max(max_side, dp[i][j])
        
        return max_side ** 2