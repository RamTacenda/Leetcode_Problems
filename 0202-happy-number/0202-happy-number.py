class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.check(n)

            if(n == 1):
                return True
            
        return False

    def check(self, num):
        temp = 0
        while(num > 0):
            rem = num % 10
            temp += rem*rem
            num //= 10
        num = temp

        return num