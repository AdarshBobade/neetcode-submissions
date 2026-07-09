class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low < high :
            mid = ( high + low )//2
            if  mid == len(nums)-1 :
                break
            if mid % 2 == 0 : # even
                if nums[mid] == nums[mid+1] :
                    low = mid + 2
                else :
                    high = mid 
            elif mid % 2 != 0 : #odd
                if nums[mid] == nums[mid - 1] :
                    low = mid + 1
                else :
                    high = mid - 1
        return nums[low]      



        