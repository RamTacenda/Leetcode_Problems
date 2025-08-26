class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if(n % 4 == 0 or n == 1):
            return True
        return False