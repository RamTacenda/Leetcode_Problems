class Solution:
    def combinations(self, idx, ds, n, k, ans):
        if(len(ds) == k):
            ans.append(ds.copy())
            return

        for i in range(idx, n+1):
            ds.append(i)
            self.combinations(i+1, ds, n, k, ans)
            ds.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = list()
        self.combinations(1, list(), n, k, ans)
        return ans