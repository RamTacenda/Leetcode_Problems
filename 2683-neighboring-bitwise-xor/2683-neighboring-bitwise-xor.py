class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ans = 0
        for num in derived:
            ans ^= num
        return True if(ans == 0) else False