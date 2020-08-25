class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res =[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum2(nums,i, res)
        return res
    
    def twoSum2(self,nums,i, res):
        left, right = i+1, len(nums)-1
        while left < right:
            summ = nums[i] + nums[left] + nums[right]
            
            if summ > 0:
                right -= 1
            elif summ < 0:
                left += 1
            else: # summ == 0
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1 #not to count same value
                
            
