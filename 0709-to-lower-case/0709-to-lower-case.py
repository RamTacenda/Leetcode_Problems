class Solution:
    def toLowerCase(self, s: str) -> str:
        s = list(s)
        for i in range(0, len(s)):
            if(s[i].isupper()):
                s[i] = chr(ord(s[i])+32)
        
        return "".join(s)