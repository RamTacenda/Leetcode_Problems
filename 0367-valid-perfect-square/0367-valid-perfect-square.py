class Solution:
    def binarySearch(self, num):
        low, high = 0, num
        while low <= high:
            mid = (low + high) // 2
            if(mid*mid <= num):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def isPerfectSquare(self, num: int) -> bool:
        ans = self.binarySearch(num)
        return True if(ans * ans == num) else False