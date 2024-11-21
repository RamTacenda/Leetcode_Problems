class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if(bills[0] != 5):
            return False
        
        fiveend = 0
        tenend = 0
        for i in bills:
            if(i == 5):
                fiveend += 1
            elif(i == 10):
                if(fiveend > 0):
                    fiveend -= 1
                else:
                    return False
                tenend += 1
            
            elif(i == 20):
                if(fiveend > 0 and tenend > 0):
                    fiveend -= 1
                    tenend -= 1
                elif(fiveend > 2):
                    fiveend -= 3
                else:
                    return False

        return True