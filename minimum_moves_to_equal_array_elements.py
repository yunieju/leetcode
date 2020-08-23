class Solution:
#     # incrementing n - 1 elements by 1 means decrementing maximum value by 1
#     # Eventually, the number of move we need is the sum of difference between the minimum and number
#     # Time Complexity: O(N)
    def minMoves(self, nums: List[int]) -> int:
        moves = 0
        minimum = min(nums)
        for i in range(0, len(nums)):
            moves += (nums[i] - minimum)
        return moves
            
#     # And we can make it more efficient without min fuction iterating one time
    
    def minMoves(self, nums: List[int]) -> int:
        moves = 0
        minimum = float('inf')
        for i in range(len(nums)):
            moves += nums[i]
            minimum = min(minimum, nums[i])
        return moves - minimum * len(nums)
    
    # DP solution
    def minMoves(self, nums:List[int]) -> int:
        nums.sort()
        dp = [0] * len(nums)
        res = 0
        for i in range(1, len(nums)):
            dp[i] = dp[i-1] + (nums[i] - nums[i-1])
            res += dp[i]
        return res
    
     # DP without extra space
    def minMoves(self, nums:List[int]) -> int:
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            diff = moves + (nums[i] - nums[i-1])
            nums[i] += moves
            moves += diff
        return moves
        
        
