class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l, r = 0, len(s)
        ans = list()
        for c in s:
            if(c == "I"):
                ans.append(l)
                l += 1
            elif(c == "D"):
                ans.append(r)
                r -= 1
        
        if(s[-1] == "I"):
            ans.append(ans[-1]+1)
        else:
            ans.append(ans[-1]-1)

        return ans