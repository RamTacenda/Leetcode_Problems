class Solution:
    def find_comb(self, idx, arr, target, ds, ans):
        # Base case
        if(idx == len(arr)):
            if(target == 0):
                ans.append(ds.copy())
            return

        if(arr[idx] <= target):
            ds.append(arr[idx])
            self.find_comb(idx, arr, (target-arr[idx]), ds, ans)
            ds.pop()

        self.find_comb(idx+1, arr, target, ds, ans)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        idx = 0
        arr = candidates
        ds = list()
        ans = list()
        self.find_comb(idx, arr, target, ds, ans)

        return ans