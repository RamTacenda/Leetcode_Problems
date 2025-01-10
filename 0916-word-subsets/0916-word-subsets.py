class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            ans = [0]*26
            for letter in word:
                ans[ord(letter)-ord('a')] += 1
            return ans

        max_freq = [0]*26
        for w2 in words2:
            for i, c in enumerate(count(w2)):
                max_freq[i] = max(max_freq[i], c)

        ans = []
        for w1 in words1:
            if all(x >= y for x, y in zip(count(w1), max_freq)):
                ans.append(w1)

        return ans