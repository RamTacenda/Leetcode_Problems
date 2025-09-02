class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        
        arr = []
        maxx = float('-inf')
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                arr.append(s[j])
                if(len(arr) == len(set(arr))):
                    if(len(arr) > maxx):
                        maxx = len(arr)
                else:
                    break
            arr.clear()

        return maxx