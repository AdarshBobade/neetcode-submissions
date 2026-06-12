class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        indices = []
        for i,x in enumerate(nums):
            diff = target - x
            if diff in hash_map:
                return [hash_map[diff] , i]
            hash_map[x] = i
                
        return 


        