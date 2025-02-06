class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        i, misplaced = 0, 0
        letters = list()
        while i < len(s1):
            if(s1[i] != s2[i]):
                misplaced += 1
                letters.extend([s1[i], s2[i]])
            i += 1

        if(misplaced in [0, 2]):
            if(misplaced  == 0):
                return True
            else:
                if(letters[0] == letters[-1] and letters[1] == letters[-2]):
                    return True
                else:
                    return False
        else:
            return False
