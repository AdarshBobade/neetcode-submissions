class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur, counter = (0,0)
        for x in nums:
            if counter == 0 :
                cur = x
            counter += (1 if x == cur else -1)
        
        return cur

        