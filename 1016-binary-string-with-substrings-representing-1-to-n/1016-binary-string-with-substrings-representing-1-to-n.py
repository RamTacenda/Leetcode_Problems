class Solution:
    def queryString(self, s: str, n: int) -> bool:
        if(n > (2**(len(s)-1))): return False
        for i in range(1, n+1):
            if(s.find(bin(i)[2:]) == -1):
                return False
        return True