class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(c**0.5)
        while l <= r:
            added = l**2 + r**2
            if(added == c):
                return True
            elif(added < c):
                l += 1
            elif(added > c):
                r -= 1
        return False