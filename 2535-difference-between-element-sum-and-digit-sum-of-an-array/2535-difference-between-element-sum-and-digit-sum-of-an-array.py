class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        e_sum = sum(nums)
        d_sum = 0
        for num in nums:
            while(num >= 1):
                rem = num % 10
                d_sum += rem
                num //= 10

        return abs(e_sum - d_sum)