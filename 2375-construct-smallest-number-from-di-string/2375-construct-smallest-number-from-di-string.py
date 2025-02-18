class Solution:
    def smallestNumber(self, pattern: str) -> str:
        num_stack = []
        res = ""

        for i in range(0, len(pattern)+1):
            num_stack.append(i+1)

            if(i == len(pattern) or pattern[i] == "I"):
                while num_stack:
                    res += str(num_stack.pop())

        return res
