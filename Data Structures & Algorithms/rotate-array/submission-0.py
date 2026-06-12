class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k = k % len(nums)
        i , j = 0 , len(nums) - 1
        while i < j :
            nums[i] , nums[j] = nums[j] , nums[i]
            i += 1
            j -= 1
        x , y = 0 , k - 1
        
        
        while x < y :
            nums[x] , nums[y] = nums[y] , nums[x]
            x += 1
            y -= 1
        
        z = len(nums) - 1
        while k < z:
            nums[k] , nums[z] = nums[z] , nums[k]
            k += 1
            z -= 1
            
        return nums
        

        