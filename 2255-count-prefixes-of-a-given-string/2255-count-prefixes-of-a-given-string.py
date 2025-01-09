class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for c in words:
            if(c == s[: len(c)]):
                count += 1
        
        return count