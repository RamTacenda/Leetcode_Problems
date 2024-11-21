class Solution:
    def GCD(self, a, b):
        if(a == 0):
            return b
        return self.GCD(b%a, a)
    def smallestEvenMultiple(self, n: int) -> int:
        return ((n*2)//self.GCD(n, 2))