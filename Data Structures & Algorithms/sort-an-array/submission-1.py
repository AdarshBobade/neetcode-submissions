class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(nums):
            if len(nums) <= 1 :
                return nums
            pivot = nums[-1]
            smaller_left = []
            larger_right = []
            for i in range(len(nums)-1):
                if nums[i] <= pivot:
                    smaller_left.append(nums[i])
                elif nums[i] > pivot:
                    larger_right.append(nums[i])
                
            smaller_left = quick_sort(smaller_left)
            larger_right = quick_sort(larger_right)
            return merge(smaller_left , pivot , larger_right)

        def merge(left,pivot,right):
            return left + [pivot] + right
        return quick_sort(nums)
        