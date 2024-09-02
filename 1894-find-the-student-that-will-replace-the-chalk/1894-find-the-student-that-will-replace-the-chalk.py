class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        totalc = sum(chalk)
        remainc = k % totalc

        for idx, c in enumerate(chalk):
            if(remainc < c):
                return idx
            remainc -= c
        
        return 0