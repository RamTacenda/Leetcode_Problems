class Solution:
    def frequencySort(self, s: str) -> str:
        mapp = dict()
        ans = list()
        for c in s:
            if(c in mapp):
                mapp[c] += 1
            else:
                mapp[c] = 1
        for c, i in sorted(mapp.items(), key = lambda x: x[1], reverse = True):
            ans.append(c*i)

        return "".join(ans)