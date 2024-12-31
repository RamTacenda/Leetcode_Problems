class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        while n > 0:
            temp = s[1:] + s[0]
            if(temp == goal):
                return True
            s = temp
            n -= 1
        
        return False

