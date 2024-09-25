class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        temp = 0
        for i in gain:
            altitude = temp+i
            print(altitude)
            ans = max(altitude, ans)
            temp = altitude
        return ans