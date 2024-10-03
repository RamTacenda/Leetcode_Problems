class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(0, len(nums)):
            if(i != 0 and nums[i] == nums[i-1]):
                continue
            left = i+1
            right = len(nums)-1
            while(left < right):
                curr = [nums[i], nums[left], nums[right]]
                summ = sum(curr)
                if(summ == 0):
                    ans.append(curr)
                    left += 1
                    right -= 1
                elif(summ > 0):
                    right -= 1
                elif(summ < 0):
                    left += 1

        return ans