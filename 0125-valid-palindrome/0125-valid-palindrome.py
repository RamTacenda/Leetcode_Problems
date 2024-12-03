class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = [c.lower() for c in s if c.isalnum()]
        return ans[::-1] == ans