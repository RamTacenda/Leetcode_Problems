class Solution:
    def find_comb(self, idx, arr, target, ds, ans):
        if(target == 0):
            ans.append(ds.copy())
            return

        for i in range(idx, len(arr)):
            if(i > idx and arr[i] == arr[i-1]): continue
            if(arr[i] > target): break

            ds.append(arr[i])
            self.find_comb(i+1, arr, (target - arr[i]), ds, ans)
            ds.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        idx = 0
        arr = sorted(candidates)
        ds = list()
        ans = list()
        self.find_comb(idx, arr, target, ds, ans)

        return ans