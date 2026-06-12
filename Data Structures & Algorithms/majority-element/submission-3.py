class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        for x in nums :
            dict1[x] = dict1.get(x,0) + 1
            
        return max(dict1 , key = dict1.get) 

        