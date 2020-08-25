class Solution:
    def titleToNumber(self, s: str) -> int:
        num = 0
        for i in range(len(s)):
            num = num * 26
            num += (ord(s[i])- ord('A') + 1)
        
        return num
