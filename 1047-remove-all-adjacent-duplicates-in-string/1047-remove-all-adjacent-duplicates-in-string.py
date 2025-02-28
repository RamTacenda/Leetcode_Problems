class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack, i = list(), 0
        while True:
            if(i == len(s)):
                return "".join(stack)
            if(stack and stack[-1] == s[i]):
                stack.pop()
            else:
                stack.append(s[i])
            i += 1