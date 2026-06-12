class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur, counter = (0,0)
        for x in nums:
            if counter == 0 :
                cur = n
            counter += (1 if n == cur else -1)
        
        return cur

        