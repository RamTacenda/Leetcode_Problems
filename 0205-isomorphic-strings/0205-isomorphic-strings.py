class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(set(s)) != len(set(t))):
            return False

        s_ls, res1 = list(), ""
        for i in range(0, len(s)):
            if(s[i] not in s_ls):
                s_ls.append(s[i])
                res1 += str(i+1)
            else:
                res1 += str(s_ls.index(s[i])+1)

        t_ls, res2 = list(), ""
        for i in range(0, len(t)):
            if(t[i] not in t_ls):
                t_ls.append(t[i])
                res2 += str(i+1)
            else:
                res2 += str(t_ls.index(t[i])+1)

        return res1 == res2