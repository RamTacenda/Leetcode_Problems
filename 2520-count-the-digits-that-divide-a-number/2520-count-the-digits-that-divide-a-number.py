class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        original = str(num)

        for digit in original:
            if(num % int(digit) == 0):
                count += 1
        return count