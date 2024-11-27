class Solution:
    def intconv(self, num):
        ans, exp = 0, 0
        for n in num[::-1]:
            ans += int(n)*(2**(exp))
            exp += 1
        return ans
    
    def binary(self, num):
        ans = ""
        while num > 0:
            ans += str(num % 2)
            num //= 2
        return ans[::-1]

    def addBinary(self, a: str, b: str) -> str:
        num = self.intconv(a) + self.intconv(b)
        if(num == 0): return a
        return self.binary(num)