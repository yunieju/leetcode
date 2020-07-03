'''
We need to check the negative numbers
two cases are available
negative * negative * positive = positive
positive * positive * positive = positive
'''

# Time complexity: O(nlogn)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        length = len(nums)
        
        nnp = sorted_nums[0] * sorted_nums[1] * sorted_nums[length - 1]      
        ppp = sorted_nums[length -1] * sorted_nums[length -2] * sorted_nums[length -3]
        
        return max(nnp, ppp)
    
 '''
We need to check the negative numbers
two cases are available
negative * negative * positive = positive
positive * positive * positive = positive

We only need to track five values.
min1, min2, max1, max2, max3
return max(min1 * min2 * max1, max1*max2*max3)
'''

# Time Complexity : O(n), Space Complexity: O(1)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1, min2 = float("inf"), float("inf")
        max1, max2, max3 = float("-inf"), float("-inf"), float("-inf")
        
        for num in nums:
            if num <= min1:
                min2 = min1
                min1 = num
            elif num <= min2: # min1 < num < min2
                min2 = num
            
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num >= max2:
                max3 = max2
                max2 = num
            elif num >= max3:
                max3 = num
   
        return max(min1*min2*max1, max1*max2*max3)
