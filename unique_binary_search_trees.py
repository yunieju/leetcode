class Solution:
    # Time Complexity: O(n^2), Space Complexity: O(N)
    def numTrees(self, n: int) -> int:
        res = [0] * (n+1)
        res[0] = 1
        for i in range(n+1):
            for j in range(i):
                res[i] += res[j] * res[i-1-j]
        return res[n]
        
            
            
            
