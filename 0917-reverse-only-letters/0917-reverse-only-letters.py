class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l, r = 0, len(s)-1
        ans = list(s)
        while l <= r:
            if(ans[l].isalpha() and ans[r].isalpha()):
                ans[l], ans[r] = ans[r], ans[l]
                l += 1
                r -= 1
            elif(ans[l].isalpha()):
                r -= 1
            elif(ans[r].isalpha()):
                l += 1
            else:
                l += 1
                r -= 1

        return "".join(ans)