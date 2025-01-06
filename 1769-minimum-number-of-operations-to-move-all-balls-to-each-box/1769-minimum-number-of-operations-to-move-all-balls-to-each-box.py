class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)
        ones = [i for i in range(0, len(boxes)) if(boxes[i] == "1")]
        for i in range(0, len(boxes)):
            for j in ones:
                ans[i] += abs(i - j)
        
        return ans