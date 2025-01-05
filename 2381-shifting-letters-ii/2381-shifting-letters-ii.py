class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        temp = [0]*n
        alpha = "abcdefghijklmnopqrstuvwxyz"
        ans = ""
        for nums in shifts:
            if(nums[2] == 1): # Increment
                temp[nums[0]] += 1
                if(nums[1]+1 < n):
                    temp[nums[1]+1] += -1
            
            else: # Decrement
                temp[nums[0]] += -1
                if(nums[1]+1 < n):
                    temp[nums[1]+1] += 1
        
        prefixsum = list()
        for i in range(0, len(temp)):
            if(i == 0):
                prefixsum.append(temp[i])
            else:
                prefixsum.append((prefixsum[-1]+temp[i]))

        for i in range(0, len(s)):
            ans += alpha[(alpha.index(s[i]) + prefixsum[i]) % 26]
        
        return ans