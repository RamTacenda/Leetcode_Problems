class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        ls, ans = s[::-1], list()
        for c in ls:
            if(c.isalpha() or c.isalnum()):
                ans.append(c)

        return " ".join(ans)
