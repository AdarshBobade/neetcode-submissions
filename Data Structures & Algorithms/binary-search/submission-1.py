class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        def Binary_Search(low,high):
            
            if low > high :
                return -1
            mid = ( low + high )//2
            if nums[mid] == target :
                return mid
            elif target > nums[mid]:
                return Binary_Search(mid+1,high)
            else :
                return Binary_Search(low,mid-1)
        return Binary_Search(low,high)

        