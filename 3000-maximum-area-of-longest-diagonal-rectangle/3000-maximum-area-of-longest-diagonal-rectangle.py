class Solution:
    def areaOfMaxDiagonal(self, dims: List[List[int]]) -> int:
        maxi = 0
        area = 0

        for i, row in enumerate(dims):
            length = row[0]
            width = row[1]
            distance = ((length**2) +  (width**2))**(0.5)
            print(f"{row}: {distance}")
            
            if distance >= maxi:
                if(distance == maxi):
                    new_area = row[0]*row[1]
                    if new_area > area:
                        area = new_area
                elif(distance > maxi):
                    print(f"distance:{distance}, Max:{maxi}")
                    maxi = distance
                    area = row[0]*row[1]
        
        return area