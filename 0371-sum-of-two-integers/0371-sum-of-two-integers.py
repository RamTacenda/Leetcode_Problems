class Solution:
    def getSum(self, a: int, b: int) -> int:
        MIN = 0x7FFFFFFF 
        MAX = 0x80000000  
        MASK = 0xFFFFFFFF
        while(b>0):
            temp = (a & b) << 1
            a = (a ^ b) & MASK
            b = (temp) & MASK

        return a if a <= MAX else ~(a ^ MASK)