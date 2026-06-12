class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i , j = (len(nums1) - n - 1) , ( len(nums2) - 1)
        k = 0

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j] :
                nums1[-1-k] =  nums1[i]
                i -= 1
                k += 1
            elif nums1[i] < nums2[j] :
                nums1[-1-k] = nums2[j]
                j -= 1
                k += 1
        

        if i < 0:
            while j >= 0:
                nums1[-1-k] = nums2[j]
                j -= 1
                k += 1



