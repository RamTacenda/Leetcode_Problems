class Solution:
    def checkPrime(self, area):
        if(area <= 1): return False
        for i in range(2, area):
            if(area % i == 0):
                return False
        return True

    def constructRectangle(self, area: int) -> List[int]:
        if(self.checkPrime(area)):
            return [area, 1]
        
        num = int(area**(0.5))
        while num >= 0:
            if(area % num == 0):
                w = num
                break
            num -= 1

        return [(area//num), w]