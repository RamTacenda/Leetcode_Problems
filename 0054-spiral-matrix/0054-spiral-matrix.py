class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        top, bottom = 0, len(mat)-1
        left, right = 0, len(mat[0])-1
        ans = list()

        while(top <= bottom and left <= right):
            # Left --> Right and top (const)
            for i in range(left, right+1):
                ans.append(mat[top][i])
            top += 1
            
            # Top --> Bottom and right (const)
            for i in range(top, bottom+1):
                ans.append(mat[i][right])
            right -= 1

            if(top <= bottom):
                # Right --> Left and bottom (const)
                for i in range(right, left-1, -1):
                    ans.append(mat[bottom][i])
                bottom -= 1

            if(left <= right):
                # Bottom --> Top and left (const)
                for i in range(bottom, top-1, -1):
                    ans.append(mat[i][left])
                left += 1

        return ans