class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        maxlen = 0

        for i in s:
            if(i == '('):
                left += 1
            else:
                right += 1
            if(left == right):
                maxlen = max(maxlen, left*2)
            elif(right > left):
                left = 0
                right = 0

        left, right = 0, 0
        for i in s[::-1]:
            if(i == '('):
                left += 1
            else:
                right += 1
            if(left == right):
                maxlen = max(maxlen, left*2)
            elif(left > right):
                left = 0
                right = 0
                
        return maxlen