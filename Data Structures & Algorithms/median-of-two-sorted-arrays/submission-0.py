class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A , B = nums1 , nums2
        if len(A) > len(B) :
            A , B = B , A
        low , high = 0 , len(A) - 1
        total = len(nums1) + len(nums2)
        half = total // 2
        while True :
            mid = (high + low)//2
            partition = (half - (mid + 1)) - 1
            Aleft = A[mid] if mid >= 0 else float("-infinity")
            Aright = A[mid + 1] if mid + 1 < len(A) else float("infinity")
            Bleft = B[partition] if partition >= 0 else float("-infinity")
            Bright = B[partition + 1] if partition + 1 < len(B) else float("infinity")
            if Aleft <= Bright and Bleft <= Aright :
                if total % 2 == 0:
                    return (max(Aleft,Bleft) + min(Bright,Aright))/2
                else :
                    return min(Aright,Bright)
            elif Aleft > Bright :
                high = mid - 1
            else :
                low = mid + 1






        