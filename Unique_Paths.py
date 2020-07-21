import math

# sol 1: using Dynamic Programming
# runtime : O(M*N) 
# space:    O(M*N)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        
        for col in range(1, m):
            for row in range(1,n):
                dp[col][row] = dp[col-1][row] + dp[col][row-1]
        return dp[m-1][n-1]
    
    

# sol 2: simple implementation with a combination concept
# space: O(1)
    def uniquePaths(self, m: int, n: int) -> int:
        return int(factorial((m-1) + (n-1)) / (factorial(m-1) * factorial(n-1)))
