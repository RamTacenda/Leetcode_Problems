class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scorecard = sorted(score, reverse = True)
        ans = [0]*len(score)
        for i in range(0, len(score)):
            pos = scorecard.index(score[i])+1
            if(pos <= 3):
                if(pos == 1):
                    ans[i] = "Gold Medal"
                elif(pos == 2):
                    ans[i] = "Silver Medal"
                else:
                    ans[i] = "Bronze Medal"
            else:
                ans[i] = str(pos)
        return ans