class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fractions = list()
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                fractions.append([(arr[i]/arr[j]), (arr[i], arr[j])])
        heapq.heapify(fractions)
        while k > 0:
            if(k == 1):
                return heapq.heappop(fractions)[1]
            heapq.heappop(fractions)
            k -= 1