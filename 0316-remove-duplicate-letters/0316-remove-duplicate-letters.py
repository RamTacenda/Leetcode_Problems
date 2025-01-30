class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occur = dict()
        for i in range(0, len(s)):
            last_occur[s[i]] = i
        
        stack = []
        visited = set()

        for i in range(0, len(s)):
            if(s[i] in visited):
                continue
            
            while stack and s[i] < stack[-1] and i < last_occur.get(stack[-1], -1):
                visited.remove(stack.pop())

            visited.add(s[i])
            stack.append(s[i])

        return "".join(stack)