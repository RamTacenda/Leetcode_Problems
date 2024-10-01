class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        # count = 0
        # left, right = 0, len(arr)-1
        # if(len(arr)&1 == 1):
        #     return False
        # while(left < right):
        #     summ = arr[left] + arr[right]
        #     if(not (summ % k == 0)):
        #         return False
        #     left += 1
        #     right -= 1
        # return True
        return (True if(sum(arr)%k == 0) else False)