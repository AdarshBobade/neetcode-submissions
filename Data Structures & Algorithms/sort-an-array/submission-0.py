class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_arr(left,right):
            i,j = 0,0
            result_ = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j] :
                    result_.append(left[i])
                    i += 1
                else:
                    result_.append(right[j])
                    j += 1
                
            return result_ + left[i:] + right[j:]
        
        def merge_sort(nums):
            n = len(nums)
            mid = n//2
            if n <= 1 :
                return nums

            left_half = nums[:mid]
            right_half = nums[mid:]

            left_half = merge_sort(left_half)
            right_half = merge_sort(right_half)

            result = merge_arr(left_half,right_half)
            return result

        return merge_sort(nums)










        