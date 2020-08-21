class Solution:
    def longestPalindrome(self, s:str)-> str:
        if len(s)< 0:
            return 0
        
        start, end = 0,0
        for i in range(len(s)):
            len1 = self.expandFromMiddle(s,i,i)
            len2 = self.expandFromMiddle(s,i,i+1)
            length = max(len1, len2)
            if length > (end - start):
                start = i - (length -1)//2
                end = i + length //2
                
        return s[start:end +1]
    
    def expandFromMiddle(self, s:str, left: int, right: int):
        if left > right: 
            return 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        return right - left - 1
    
    #Brute Force: Time Complexity: O(n^3) -> TLE
#     def longestPalindrome(self, s: str) -> str:
#         res = ""
#         for i in range(len(s)): # substring starts from index i
#             substring = ""
#             for j in range(i, len(s)):
#                 substring += s[j]
#                 if self.checkPalindrome(substring):
#                     if len(substring) > len(res):
#                         res = substring
#         return res
    
#     def checkPalindrome(self, sub: str)-> bool:
#         return sub[::-1] == sub
        
