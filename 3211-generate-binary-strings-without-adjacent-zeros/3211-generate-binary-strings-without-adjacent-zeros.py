class Solution:
    def bin_Strings(self, idx, n, ds, ans):
        if(idx == n):
            ans.append("".join(ds))
            return
        
        ds.append("1")
        self.bin_Strings(idx+1, n, ds, ans)
        ds.pop()

        if(ds and ds[-1] == "0"):
            return
        ds.append("0")
        self.bin_Strings(idx+1, n, ds, ans)
        ds.pop()

    def validStrings(self, n: int) -> List[str]:
        ans = list()
        self.bin_Strings(0, n, list(), ans)
        return ans
        