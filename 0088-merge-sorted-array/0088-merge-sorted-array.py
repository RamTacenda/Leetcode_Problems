class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n <= 0:
            return nums1
        
        temp = nums1[:m] + nums2
        temp.sort()
        for i in range(0, len(temp)):
            nums1[i] = temp[i]
        