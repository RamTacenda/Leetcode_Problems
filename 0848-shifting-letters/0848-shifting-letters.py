class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        ans = ""
        prefix = [shifts[-1]]
        for i in range(len(shifts)-2, -1, -1):
            prefix.append(shifts[i]+prefix[-1])

        prefixsum = prefix[::-1]

        for i in range(0, len(s)):
            ans += alpha[(alpha.index(s[i]) + prefixsum[i]) % 26]
        
        return ans