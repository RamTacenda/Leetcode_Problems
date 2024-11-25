class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s)-1
        ans = list(s)
        vowels = "aeiou"

        while l <= r:
            if(ans[l].lower() in vowels and ans[r].lower() in vowels):
                ans[l], ans[r] = ans[r], ans[l]
                l += 1
                r -= 1
            elif(ans[l].lower() in vowels):
                r -= 1
            elif(ans[r].lower() in vowels):
                l += 1
            else:
                l += 1
                r -= 1

        return "".join(ans)