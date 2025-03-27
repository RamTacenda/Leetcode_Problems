class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        mapp = defaultdict(int)
        for n in nums:
            mapp[n] += 1
        maximum = 0
        element = 0
        for key, val in mapp.items():
            if(val > maximum):
                maximum = val
                element = key

        n = len(nums)
        # Finding prefix sum
        prefixsum = [0]*n
        for i in range(0, n):
            if(i == 0):
                prefixsum[i] = 1 if(nums[i] == element) else 0
            else:
                val = 1 if(nums[i] == element) else 0
                prefixsum[i] += prefixsum[i-1] + val
        print(prefixsum)


        for i in range(1, n):
            left_count, right_count = prefixsum[i-1], (maximum - prefixsum[i-1])
            # print(f"left part: {nums[:i], i} and left count: {left_count}")
            # print(f"right part: {nums[i:], n-i} and right count: {right_count}")
            if(left_count*2 > i and right_count*2 > n-i):
                return i-1
            # print()

        return -1