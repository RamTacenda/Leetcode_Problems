class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)==1:
            return [-1]
        
        ans = [-1, arr[len(arr)-1]]
        maxx = arr[len(arr)-1]
        for i in range(len(arr)-2,0,-1):
            maxx = max(maxx, arr[i])
            ans.append(maxx)

        return ans[::-1]