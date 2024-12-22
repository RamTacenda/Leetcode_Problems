class Solution(object):
    def maxSlidingWindow(self, nums, k):
        q = deque()
        res = []

        for i in range(0, len(nums)):
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])

            if(i >= k and nums[i-k] == q[0]):
                q.popleft()
            
            if(i >= k-1):
                res.append(q[0])

        return res