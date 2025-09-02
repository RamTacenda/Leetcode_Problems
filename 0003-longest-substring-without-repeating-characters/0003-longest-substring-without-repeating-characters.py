class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset, maximum = set(), 0
        for i in range(0, len(s)):
            j = i
            while(j < len(s) and s[j] not in hashset):
                hashset.add(s[j])
                j += 1
            maximum = max(maximum, j-i)
            hashset.clear()
        
        return maximum
