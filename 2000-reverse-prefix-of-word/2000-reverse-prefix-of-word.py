class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = ""
        for i in range(0, len(word)):
            if word[i] == ch:
                ans += word[:i+1][::-1]
                ans += word[i+1:]
                break
        return ans if ans else word