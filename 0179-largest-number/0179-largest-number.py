class Solution:
    def largestNumber(self, numbers: List[int]) -> str:
        nums = list(map(str, numbers))
        nums.sort(key = lambda x: x*10, reverse = True)
        return str(int("".join(nums)))