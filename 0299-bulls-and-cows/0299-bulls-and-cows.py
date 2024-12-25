class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        indices = list()
        for i in range(0, len(secret)):
            if(secret[i] == guess[i]):
                bulls += 1
                indices.append(i)

        mapp = defaultdict(int)
        for i in range(0, len(secret)):
            if(i not in indices):
                mapp[secret[i]] += 1

        print(mapp)
        for j in range(0, len(guess)):
            if(j not in indices and guess[j] in mapp):
                if(mapp[guess[j]] != 0):
                    cows += 1
                    mapp[guess[j]] -= 1

        print(mapp)
        return f"{bulls}A{cows}B"