class Solution:
    # time: O(M+N)
    # space: O(1)
    def backspaceCompare(self, S: str, T: str) -> bool:
        p1, p2 = len(S) - 1, len(T) - 1
         
        count = 0
        while p1 >= 0 or p2 >= 0:
            while p1 >= 0:
                if S[p1] == "#":
                    count += 1
                    p1 -= 1
                elif S[p1] != "#" and count > 0:
                    count -= 1
                    p1 -= 1
                else:
                    break
                    
            while p2 >= 0:
                if T[p2] == "#":
                    count += 1
                    p2 -= 1
                elif T[p2] != "#" and count > 0:
                    count -= 1
                    p2 -= 1
                else:
                    break
            
            if (p1 < 0 and p2 >= 0) or (p1 >= 0 and p2 < 0):
                return False
            if (p1 >= 0 and p2 >= 0) and S[p1] != T[p2]:
                return False
             
            p1 -= 1
            p2 -= 1
        return True
        
    # using two stacks 
    # time : O(M+N)
    # space : O(M+N)
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1= []
        for char in S:
            if char != "#":
                stack1.append(char)
            elif char == "#" and len(stack1) >= 1:
                stack1.pop()
                
        stack2 = []
        for char in T:
            if char != "#":
                stack2.append(char)
            elif char == "#" and len(stack2) >= 1:
                stack2.pop()
        return stack1 == stack2
