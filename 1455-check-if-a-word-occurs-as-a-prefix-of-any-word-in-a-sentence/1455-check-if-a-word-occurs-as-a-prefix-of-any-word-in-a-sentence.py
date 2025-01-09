class Solution:
    def isPrefixOfWord(self, sent: str, word: str) -> int:
        words = list()
        temp = ""
        for i in range(0, len(sent)):
            if(sent[i] != " "):
                temp += sent[i]
            elif(sent[i] == " "):
                words.append(temp)
                temp = ""
        words.append(temp)

        n = len(word)
        for idx, w in enumerate(words):
            if(w[:n] == word):
                return idx+1
        return -1