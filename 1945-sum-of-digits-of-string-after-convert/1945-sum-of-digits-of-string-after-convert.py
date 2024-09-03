class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = ""
        ans = 0
        fans = 0
        for i in s:
            nums += str((ord(i)-96))

        for _ in range(0, k):
            for i in nums:
                print(i, end = " ")
                ans += int(i)
            nums = str(ans)
            fans = ans
            ans = 0
        
        return int(fans)