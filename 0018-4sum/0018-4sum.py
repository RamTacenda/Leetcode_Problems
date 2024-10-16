class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(0, len(nums)):
            if(i != 0 and nums[i-1] == nums[i]): continue
            for j in range(i+1, len(nums)):
                if(j != i+1 and nums[j-1] == nums[j]): continue

                left = j+1
                right = len(nums)-1

                while(left < right):
                    ls = [nums[i], nums[j], nums[left], nums[right]]
                    summ = sum(ls)
                    if(summ == target):
                        res.append(ls)
                        left += 1
                        right -= 1
                        while(left < right and nums[left] == nums[left-1]): 
                            left += 1
                        while(left < right and nums[right] == nums[right+1]):
                            right -= 1
                    
                    elif(summ > target):
                        right -= 1
                    
                    elif(summ < target):
                        left += 1

        return res