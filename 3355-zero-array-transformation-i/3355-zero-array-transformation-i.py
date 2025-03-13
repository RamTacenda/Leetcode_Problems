class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        check = [0]*(n+1)
        for q in queries:
            check[q[0]] += 1
            check[q[1]+1] -= 1
        
        print(check)

        for i in range(1, len(check)):
            check[i] += check[i-1]
        
        for j in range(0, len(nums)):
            if(check[j] < nums[j]):
                return False
        return True