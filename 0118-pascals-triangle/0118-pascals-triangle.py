class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = list()
        for i in range(0, numRows):
            p = 1
            temp = []
            for j in range(0, i+1):
                temp.append(p)
                p = p*(i-j) // (j+1)
            ans.append(temp)
            
        return ans