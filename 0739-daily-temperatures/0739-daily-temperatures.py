class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        ans = [0]*len(arr)
        stack = []

        for i, t in enumerate(arr):
            while stack and stack[-1][0]<t:
                stack_t, stack_idx = stack.pop()
                ans[stack_idx] = i-stack_idx
            stack.append((arr[i], i))
        
        return ans