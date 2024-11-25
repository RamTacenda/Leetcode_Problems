class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split(" ")
        ans = ""
        for s in ls:
            ans += s[::-1] + " "
        
        return ans.strip()