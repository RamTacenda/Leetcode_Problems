class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = list()
        part = list(part)
        last = part[-1]
        for c in s:
            if(len(part) == 1 and c == part[0]):
                continue
            elif(c == last and stack[-len(part)+1: ] == part[:-1]):
                stack = stack[:-len(part)+1]
            else:
                stack.append(c)
        
        return "".join(stack)