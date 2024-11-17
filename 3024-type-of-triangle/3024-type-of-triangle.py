class Solution:
    def triangleType(self, nums: List[int]) -> str:

        if(len(set(nums)) == 1):
            its_type = "equilateral"
        elif(len(set(nums)) == 2):
            its_type = "isosceles"
        else:
            its_type = "scalene"

        if((nums[1]+nums[0] > nums[2]) and (nums[0]+nums[2] > nums[1]) and (nums[2]+nums[1] > nums[0])):
            return its_type
        else:
            return "none"
        
