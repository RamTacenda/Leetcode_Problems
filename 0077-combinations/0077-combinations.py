class Solution:
    def combinations(self, idx, ds, n, k, res):
        if(len(ds) == k):
            res.append(ds.copy())
            return

        for i in range(idx, n+1):
            ds.append(i)
            self.combinations(i+1, ds, n, k, res)
            ds.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = list()
        self.combinations(1, list(), n, k, res)
        return res