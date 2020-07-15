class Solution:
#     def numSub(self, s: str) -> int:
#         count = 0
#         for i in range(len(s)):
#             while i < len(s) and s[i] == "1":
#                 count += 1
#                 i += 1
                
#         return count
    
    # using arithmatic sum   
    def numSub(self, s:str) -> int:
        count = 0
        counts = []
        total = 0
        
        for i in range(len(s)):
            if s[i] == "1":
                count += 1
            else:
                counts.append(count)
                count = 0
        counts.append(count)
        
        for count in counts:
            subs = count * (count + 1) // 2
            total += subs
        # Since the answer may be too large, return it modulo 10^9 + 7.
        total = total % (10**9 + 7)
        return  total


                
