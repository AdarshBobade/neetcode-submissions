class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        seen = []
        for x in nums:
            if x not in seen :
                dict1[x] = nums.count(x)
                seen.append(x)
            
        
        return max(dict1)

        