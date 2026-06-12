class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        idx = 0
        while idx < len(nums):
            if nums[idx] == idx + 1:
                idx += 1
            elif 1 <= nums[idx] <=len(nums) and nums[nums[idx]-1] != nums[idx]:
                correct_idx = nums[idx] - 1
                nums[idx], nums[correct_idx] = nums[correct_idx], nums[idx]
            else :
                idx += 1
            
        fmp = len(nums) + 1
        for index,value in enumerate(nums):
            if value != index + 1:
                fmp = index + 1
                break
            
        return fmp

        