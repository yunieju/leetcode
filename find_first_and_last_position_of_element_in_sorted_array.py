class Solution:
    def findStartingIndex(self,nums, target):
        idx = -1
        l = 0
        r = len(nums)-1
        
        while l <= r:
            m = l + (r-l)//2
            if nums[m] >= target:
                r = m - 1
            else:
                l += 1
            if nums[m] == target:
                idx = m
        return idx
    
    def findEndingIndex(self,nums, target):
        idx = -1
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = l + (r-l)//2
            if nums[m] <= target:
                l = m+1
            else:
                r -= 1
            if nums[m] == target:
                idx = m
        return idx
    
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        res[0] = self.findStartingIndex(nums, target)
        res[1] = self.findEndingIndex(nums, target)
        return res
