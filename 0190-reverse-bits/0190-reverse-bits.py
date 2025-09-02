class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(0, 32):
            ans = (ans << 1) | (n&1)
            n >>= 1
        return ans