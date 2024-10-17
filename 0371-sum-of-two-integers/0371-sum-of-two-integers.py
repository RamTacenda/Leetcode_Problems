class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Constants for 32-bit integers
        MAX = 0x7FFFFFFF  # This is 2,147,483,647 (maximum positive integer in 32-bit)
        MIN = 0x80000000  # This is -2,147,483,648 (minimum negative integer in 32-bit)
        MASK = 0xFFFFFFFF # This is 32-bits of all 1s (4294967295 in decimal)

        while b != 0:
            # Calculate the carry
            temp = (a & b) << 1
            
            # XOR will give the sum without carry
            a = (a ^ b) & MASK
            
            # Carry is shifted left, stored in b
            b = temp & MASK

        # If a is greater than the maximum positive 32-bit value, 
        # we interpret it as a negative number by using two's complement.
        return a if a <= MAX else ~(a ^ MASK)
