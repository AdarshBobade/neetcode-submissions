class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def BinarySearch(low , high):
            while low <= high :
                mid = (high + low)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target :
                    high = mid - 1
                else :
                    low = mid + 1
            return -1
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (high + low) // 2
            if nums[mid] <= nums[high]:
                high = mid
            else:
                low = mid + 1
        cut = low
        if cut == 0 :
            return BinarySearch(low=0 , high = (len(nums)-1))
        if nums[0] > target :
            low = cut 
            high = len(nums) - 1
            return BinarySearch(low , high)
        elif nums[0] < target :
            low = 0
            high = cut - 1
            return BinarySearch(low , high)
        elif nums[0] == target :
            return 0
        else :
            return -1









