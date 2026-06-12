class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = []
        for i in range(len(nums)):
            if nums[i] in dup:
                return True
            
            else :
                dup.append(nums[i])

        return False




