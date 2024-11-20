class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while(n not in visit):
            visit.add(n)
            
            temp = 0
            while(n > 0):
                rem = n % 10
                temp += rem*rem
                n //= 10
            n = temp

            if(n == 1): return True
        
        return False