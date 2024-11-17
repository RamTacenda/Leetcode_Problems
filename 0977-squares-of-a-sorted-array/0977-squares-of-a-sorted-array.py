class Solution:
    def power(self, exp, base):
        res = 1
        while(exp > 0):
            if(exp & 1 == 1):
                res *= base
            exp = exp >> 1
            base *= base
        return res

    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            nums[i] = self.power(2, nums[i])

        nums.sort()
        return nums