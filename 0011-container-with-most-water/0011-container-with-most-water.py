class Solution:
    def maxArea(self, height: List[int]) -> int:
        arr = height.copy()
        l = 0
        r = len(height)-1
        maxArea = 0

        while(l < r):
            area = min(arr[l], arr[r]) * (r-l)
            maxArea = max(maxArea, area)

            if(arr[l] < arr[r]):
                l += 1
            else:
                r -= 1
        
        return maxArea