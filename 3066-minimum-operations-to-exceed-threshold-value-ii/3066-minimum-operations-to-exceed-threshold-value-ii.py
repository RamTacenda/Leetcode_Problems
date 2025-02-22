class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapq.heapify(nums)
        while True:
            num1 = heapq.heappop(nums)
            if(num1 >= k):
                return count
            num2 = heapq.heappop(nums)
            new_num = (num1*2 + num2)
            count += 1
            heapq.heappush(nums, new_num)