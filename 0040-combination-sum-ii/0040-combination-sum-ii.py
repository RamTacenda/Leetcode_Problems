class Solution:
    def find_comb(self, idx, target, arr, ds, ans):
        if(target == 0):
            ans.append(ds.copy())
            return

        for i in range(idx, len(arr)):
            if(i > idx and arr[i] == arr[i-1]): continue
            if(arr[i] > target): break

            ds.append(arr[i])
            self.find_comb(i+1, (target-arr[i]), arr, ds, ans)
            ds.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ds = list()
        ans = list()
        candidates.sort()
        self.find_comb(0, target, candidates, ds, ans)
        return ans