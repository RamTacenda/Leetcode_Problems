class Solution:
    def f(self, i, j, p, t, memo):
        if((i,j) in memo):
            return memo[(i,j)]
        if(i < 0 and j < 0): return True
        if(i < 0 and j >=0): return False
        if(j < 0 and i >= 0):
            for idx in range(0, i+1):
                if(p[idx] != "*"):
                    return False
            return True

        if(p[i] == t[j] or p[i] == '?'):
            memo[(i,j)] = self.f(i-1, j-1, p, t, memo)
            return memo[(i,j)]

        if(p[i] == "*"):
            memo[(i,j)] = self.f(i-1, j, p, t, memo) or self.f(i, j-1, p, t, memo)
            return memo[(i,j)]

    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        memo = {}
        return self.f(m-1, n-1, p, s, memo)