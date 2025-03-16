class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 1, max(ranks)*(cars)*(cars)
        while left <= right:
            mid = (left + right) // 2
            summ = 0
            for r in ranks:
                summ += math.floor(math.sqrt(mid // r))
            print(f"Sum : {summ} and Mid : {mid}")
            if summ >= cars:
                ans = summ
                right = mid - 1
            else:
                left = mid + 1
        
        return left
