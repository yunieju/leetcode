class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        
        while numBottles >= numExchange:
            numBottles, r = divmod(numBottles, numExchange)
            total += numBottles
            numBottles += r
            
        return total
