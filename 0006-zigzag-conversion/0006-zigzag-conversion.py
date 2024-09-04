class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows <= 1 or numRows >= len(s)):
            return s

        idx, d = 0, 1
        res = [[] for _ in range(0, numRows)]
        for char in s:
            res[idx].append(char)
            if(idx == 0):
                d = 1
            elif(idx == numRows-1):
                d = -1
            idx += d

        fres = []
        for i in res:
            fres += i
        return "".join(fres)