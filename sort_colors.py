class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = cur = 0
        r = len(nums) -1
        
        while cur <= r:
            if nums[cur] == 0:
                nums[l], nums[cur] = nums[cur], nums[l]
                l += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[r] = nums[r], nums[cur]
                r -=1 
            else:
                cur += 1
                
    # two pass algorithm
    def sortColors(self, nums: List[int]) -> None:        
        color = [0] *3
        for num in nums:
            color[num] += 1
        
        idx = 0
        for i in range(3):
            for _ in range(color[i]):
                nums[idx] = i
                idx += 1
            
                
