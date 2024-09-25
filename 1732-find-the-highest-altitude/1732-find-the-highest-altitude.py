class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        temp = 0
        for val in gain:
            altitude = temp+val
            ans = max(ans, altitude)
            temp = altitude
        return ans