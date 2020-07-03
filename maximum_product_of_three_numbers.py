'''
We need to check the negative numbers
two cases are available
negative * negative * positive = positive
positive * positive * positive = positive
'''

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        length = len(nums)
        
        nnp = sorted_nums[0] * sorted_nums[1] * sorted_nums[length - 1]      
        ppp = sorted_nums[length -1] * sorted_nums[length -2] * sorted_nums[length -3]
        
        return max(nnp, ppp)
