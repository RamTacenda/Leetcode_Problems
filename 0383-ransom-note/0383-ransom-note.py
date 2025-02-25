class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map_rn, map_mg = dict(), dict()
        for c in ransomNote:
            map_rn[c] = map_rn.get(c, 0) + 1
        for c in magazine:
            map_mg[c] = map_mg.get(c, 0) + 1

        for k, v in map_rn.items():
            if(k not in map_mg):
                return False
            if(v > map_mg[k]):
                return False
        return True