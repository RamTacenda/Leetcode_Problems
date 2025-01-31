class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if(p1 == p3 and p2 == p4 or p1 == p2 and p3 == p4): return False
        # Euclidean Distance
        def dist(p1, p2):
            dist = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
            return dist

        # Square has excatly two unique distances (Side Length and Diagnol Length)
        distances = set()
        diagnols = set()
        points = [p1, p2, p3, p4]
        for i in range(0, len(points)):
            for j in range(i+1, len(points)):
                distance = dist(points[i], points[j])
                distances.add(distance)
                if((i, j) == (0, 2) or (i, j) == (1, 3)):
                    diagnols.add(distance)
        
        return True if(len(distances) == 2 and len(diagnols) == 1) else False