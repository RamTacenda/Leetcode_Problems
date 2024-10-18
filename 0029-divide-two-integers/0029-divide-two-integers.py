class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        sign = True
        if(dividend == divisor): return 1
        if(dividend >= 0 and divisor < 0): sign = False
        if(dividend < 0 and divisor > 0): sign = False

        n, d = abs(dividend), abs(divisor)
        while(n >= d):
            count = 0
            while(n >= (d << count)):
                count += 1
            
            ans += (1 << (count-1))
            n -= (d << (count-1))

        if(ans >= 2**31):
            if(sign):
                return (2**31)-1
            else:
                return -(2**31)
        
        return ans if(sign) else -ans