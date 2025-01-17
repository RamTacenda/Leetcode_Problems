class Solution:
    def minLength(self, s: str) -> int:
        stack = list()
        for c in s:
            if(stack and c == "B"):
                if(stack[-1] == "A"):
                    stack.pop()
                    continue
            elif(stack and c == "D"):
                if(stack[-1] == "C"):
                    stack.pop()
                    continue
            stack.append(c)
        
        return len(stack)