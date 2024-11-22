class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        i = 0
        while(True):
            p, temp = 1, list()
            for j in range(0, i+1):
                temp.append(p)
                p = p*(i-j)//(j+1)
            if(i == rowIndex):
                return temp
            i += 1
