class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        mapp = dict()
        count = 0
        for i in answers:
            mapp[i] = 1 + mapp.get(i, 0)
        
        for x, y in zip(mapp.keys(), mapp.values()):
            count += ceil(y/(x+1))*(x+1)

        return count