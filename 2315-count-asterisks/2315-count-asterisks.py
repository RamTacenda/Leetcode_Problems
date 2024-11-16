class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        check = True
        mapp = ["&"]
        for c in s:
            if(c == "|"):
                if(mapp[-1] == "|"):
                    mapp.pop()
                    check = True
                else:
                    mapp.append("|")
                    check = False
            
            elif(c == "*" and check == True):
                count += 1

        return count