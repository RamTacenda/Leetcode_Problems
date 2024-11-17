class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        overall_sum = (n*(n+1))//2
        divisible_m_sum = sum([i for i in range(1, n+1) if(i % m == 0)])
        return (overall_sum - (2*divisible_m_sum))