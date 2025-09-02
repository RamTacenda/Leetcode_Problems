class Solution:
    def isValid(self, s: str) -> bool:
        openls = "([{<"
        closels = ")]}>"
        stack = []
        check = 0

        if(s[0] in closels): return False

        for i in range(0, len(s)):
            if(s[i] in openls):
                stack.append(s[i])
            else:
                pos = closels.index(s[i])
                if(len(stack) > 0 and stack[-1] == openls[pos]):
                    stack.pop()
                else:
                    check += 1

        if(not stack and check == 0):
            return True
        else:
            return False