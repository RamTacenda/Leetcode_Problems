class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        prev = intervals[0]

        for interval in intervals[1:]:
            if(prev[1] >= interval[0]):
                prev[1] = max(interval[1], prev[1])
            else:
                merged.append(prev)
                prev = interval
        
        merged.append(prev)
        return merged
