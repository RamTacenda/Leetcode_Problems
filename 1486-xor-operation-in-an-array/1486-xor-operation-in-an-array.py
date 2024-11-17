class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = [(start + 2 * i) for i in range(0, n)]
        ans = 0
        for num in arr:
            ans ^= num
        
        return ans