class Solution:
    # Time Complexity: O(N), Space Complexity: O(N)
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set([])
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
   

     # Time Complexity: O(NlogN), Space Complexity: O(1)
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
