class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = float('inf')
        for char in strs:
            minlen = min(len(char), minlen)

        i = 0
        for i in range(0, minlen):
            for s in strs[1:]:
                if(s[i] != strs[0][i]):
                    return s[:i]
        
        return strs[0][:i]
        

        
