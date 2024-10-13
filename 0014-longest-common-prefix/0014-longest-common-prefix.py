class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = float('inf')
        for char in strs:
            minlen = min(len(char), minlen)

        i = 0
        while(i < minlen):
            for s in strs:
                if(s[i] != strs[0][i]):
                    return s[:i]
            i += 1
        
        return strs[0][:i]
        

        
