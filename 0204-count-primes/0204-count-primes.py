class Solution:
    def countPrimes(self, n: int) -> int:
        if(n in (0, 1, 2)):
            return 0

        prime = [1]*(n)
        prime[0] = prime[1] = 0

        for i in range(2, int(n**0.5)+1):
            if(prime[i] == 1):
                for j in range(i*i, n, i):
                    prime[j] = 0

        return prime.count(1)