class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Seive of Erastothenisis
        prime = [1]*(right+1)
        prime[0] = prime[1] = 0
        for i in range(2, int(right**0.5)+1):
            if(prime[i] == 1):
                for j in range(i*i, len(prime), i):
                    prime[j] = 0
        ans = list()
        for i in range(left, right+1):
            if(prime[i] == 1):
                ans.append(i)

        if(not ans or len(ans) == 1):
            return [-1, -1]
        

        minval = float('inf')
        res = [0, 0]
        for i in range(0, len(ans)-1):
            val = (ans[i+1] - ans[i])
            if(val < minval):
                minval = val
                res[0], res[1] = ans[i], ans[i+1]

        return res