class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefixsum, ans = list(), list()
        vowels = "aeiou"
        count = 0
        for word in words:
            if(word[0] in vowels and word[-1] in vowels):
                count += 1
            prefixsum.append(count)

        for q in queries:
            if(q[0] == 0):
                ans.append(prefixsum[q[-1]])
            else:
                ans.append((prefixsum[q[-1]] - prefixsum[q[0]-1]))
        return ans