class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = float('-inf')
        for sent in sentences:
            ans = max(len(sent.split(" ")), ans)
        return ans