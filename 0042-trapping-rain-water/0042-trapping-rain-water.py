class Solution:
    def trap(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        maxl, maxr = 0, 0
        ans = 0

        while(l < r):
            if(arr[l] < arr[r]):
                if(arr[l] > maxl):
                    maxl = arr[l]
                else:
                    ans += maxl - arr[l]

                l += 1

            else:
                if(arr[r] > maxr):
                    maxr = arr[r]
                else:
                    ans += maxr - arr[r]

                r -= 1
            
        return ans