class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(nums):
            if len(nums) <= 1 :
                return nums
            first = nums[0]
            mid = nums[len(nums)//2]
            last = nums[-1]
            pivot = sorted([first, mid, last])[1]

            smaller_left = []
            larger_right = []
            equal = []

            for i in range(len(nums)):
                if nums[i] < pivot:
                    smaller_left.append(nums[i])
                elif nums[i] > pivot:
                    larger_right.append(nums[i])
                else:
                    equal.append(nums[i])
                
            smaller_left = quick_sort(smaller_left)
            larger_right = quick_sort(larger_right)
            return smaller_left + equal + larger_right

        # def merge(left,pivot,right):
        #     return left + [pivot] + right
        return quick_sort(nums)
        