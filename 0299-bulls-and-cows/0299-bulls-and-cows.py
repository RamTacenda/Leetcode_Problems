class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        for i in range(0, len(secret)):
            if(secret[i] == guess[i]):
                bulls += 1

        for j in set(secret):
            cows += min(secret.count(j), guess.count(j))
        return f"{bulls}A{cows - bulls}B"