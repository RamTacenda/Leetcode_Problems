class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans, exp = 0, 0
        for c in columnTitle[::-1]:
            ans += (ord(c)-64) * (26**(exp))
            exp += 1

        return ans