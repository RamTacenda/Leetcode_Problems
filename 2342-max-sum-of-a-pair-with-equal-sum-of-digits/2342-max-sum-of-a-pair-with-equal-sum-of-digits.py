class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Calculating Sum of digits
        def digitSum(n):
            res = 0
            while n > 0:
                res += n % 10
                n //= 10
            return res

        mapp = defaultdict(SortedList)
        for i in range(0, len(nums)):
            total = digitSum(nums[i])
            mapp[total].add(nums[i])

        print(mapp)
        ans = -1
        for val in mapp.values():
            if(len(val) >= 2):
                summ = val[-1] + val[-2]
                if(summ > ans):
                    ans = summ

        return ans