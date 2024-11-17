class Solution:
    def checkIfPangram(self, sent: str) -> bool:
        if(len(list(set(sent))) == 26):
            return True
        else:
            return False