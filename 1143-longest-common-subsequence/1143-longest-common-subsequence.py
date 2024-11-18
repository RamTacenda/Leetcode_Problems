class Solution:
    def lcs(self, s, t, idx1, idx2, memo):
        if(idx1 < 0 or idx2 < 0): return 0

        if((idx1, idx2) in memo):
            return memo[(idx1, idx2)]
        
        if(s[idx1] == t[idx2]):
            memo[(idx1, idx2)] = 1 + self.lcs(s, t, idx1-1, idx2-1, memo)
        else:
            memo[(idx1, idx2)] = max(self.lcs(s, t, idx1-1, idx2, memo), self.lcs(s, t, idx1, idx2-1, memo))

        return memo[(idx1, idx2)]
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        memo = {}
        ans = self.lcs(s, t, len(s)-1, len(t)-1, memo)
        return ans