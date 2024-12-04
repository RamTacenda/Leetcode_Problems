class Solution:
    def toHex(self, num: int) -> str:
        hexas = "0123456789abcdef"
        
        if(num >= 0 and num <= 15):
            return hexas[num]
        
        if(num < 0):
            num += 2**32

        res = ""

        while num > 0:
            res += hexas[num % 16]
            num //= 16

        return res[::-1]