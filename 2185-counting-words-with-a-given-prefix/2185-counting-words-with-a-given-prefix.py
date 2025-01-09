class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count, n = 0, len(pref)
        for word in words:
            if(word[:n] == pref):
                count += 1

        return count