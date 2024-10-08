class Solution:
    def isValid(self, s: str) -> bool:
        openls = "{[("
        closels = "}])"
        stack = []
        c = 0
        if(len(s) <= 1 or s[0] in closels):
            return False
        for i in s:
            if(i in openls):
                stack.append(i)
            elif(i in closels):
                pos = closels.index(i)
                if(len(stack) > 0 and openls[pos] == stack[-1]):
                    stack.pop()
                # elif(len(stack) > 0 and openls[pos] != stack[-1]):
                else:
                    c += 1
        
        if(len(stack) == 0 and c == 0):
            return True
        else:
            return False