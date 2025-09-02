class Solution:
    def getSum(self, a: int, b: int) -> int:
        check = False
        if(a < 0 and b >= 0):
            check = True
            a, b = 0-a, 0-b

        while(b != 0):
            temp = (a & b) << 1
            a = (a ^ b)
            b = (temp)

        if check:
            return 0-a
        
        return a