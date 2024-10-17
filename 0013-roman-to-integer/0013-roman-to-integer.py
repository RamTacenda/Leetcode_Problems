class Solution:
    def romanToInt(self, s: str) -> int:
        mapp = {
            "I": 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        res = 0
        for i in range(0, len(s)-1):
            if(mapp[s[i]] < mapp[s[i+1]]):
                res -= mapp[s[i]]
            else:
                res += mapp[s[i]]

        res += mapp[s[-1]]
        return res