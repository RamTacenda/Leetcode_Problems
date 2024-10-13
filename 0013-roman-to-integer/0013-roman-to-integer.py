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
        for a, b in zip(s, s[1:]):
            if(mapp[a] < mapp[b]):
                res -= mapp[a]
            else:
                res += mapp[a]

        res += mapp[b]
        return res