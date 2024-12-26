class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = float('inf')
        small = ""
        for string in strs:
            if(len(string) < minlen):
                minlen = len(string)
                small = string

        ans, i = "", 0
        while minlen > 0:
            for word in strs:
                if(small[i] != word[i]):
                    return ans
            ans += small[i]
            i += 1
            minlen -= 1

        return ans