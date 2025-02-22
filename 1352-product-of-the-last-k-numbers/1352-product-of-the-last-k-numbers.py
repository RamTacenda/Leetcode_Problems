class ProductOfNumbers:

    def __init__(self):
        self.nums = list()
        
    def add(self, num: int) -> None:
        if not self.nums:
            self.nums.append(num)
        else:
            if(self.nums[-1] == 0):
                self.nums.clear()
                self.nums.append(num)
            else:
                self.nums.append(self.nums[-1] * num)

    def getProduct(self, k: int) -> int:
        nume = self.nums[-1]
        if(len(self.nums) == k):
            return nume
        if(len(self.nums) < k):
            return 0
        deno = self.nums[-(k+1)]
        return nume // deno


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)