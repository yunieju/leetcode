class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = ""
        cur_string = ""
        ans = ""
        for c in s:
            if c == "]":
                while stack[-1] != "[":
                    cur_string = stack.pop() + cur_string
               
                stack.pop() #pop "["
                # cur_num = stack.pop()
                while stack and stack[-1].isdigit():
                    cur_num = stack.pop() + cur_num
                stack.append(cur_string * int(cur_num))
                cur_string = ""
                cur_num = ""
            else: 
                stack.append(c)
        return "".join(stack)
