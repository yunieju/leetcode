class Solution:
    def isSubsequence1(self, s: str, t: str) -> bool:
        for c in s:
            if len(t) == 0:
                return False
            for i in range(len(t)):
                if c not in t[i:]:
                    return False
                if c == t[i]:
                    t = t[i+1:]
                    break
        return True
                
    # Greedy + Divide and conquer    
    def isSubsequence2(self,s: str, t:str) -> bool:
        L_BOUND , R_BOUND = len(s), len(t)
        
        def check(left_index, right_index):
            if left_index == L_BOUND:
                return True
            if right_index == R_BOUND:
                return False
            
            if s[left_index] == t[right_index]:
                left_index += 1
            right_index += 1
            
            return check(left_index, right_index)
        return check(0,0)
