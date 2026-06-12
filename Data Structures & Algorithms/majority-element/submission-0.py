class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        for x in nums:
            
            dict1[x] = nums.count(x)

        

        return max(dict1)

        