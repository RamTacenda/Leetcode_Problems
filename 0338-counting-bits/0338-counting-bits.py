class Solution:
    def countBits(self, n: int) -> List[int]:
        def countBits(num):
            count = 0
            while num:
                if(num%2):
                    count += 1
                num //= 2
            return count

        ans = [countBits(i) for i in range(0, n+1)]
        return ans
