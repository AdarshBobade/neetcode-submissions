class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        cur = 0
        for num in hash_set :
            ptr = num
            new = 1
            if ptr - 1 not in hash_set :
                while ptr + 1 in hash_set :
                    new += 1
                    ptr = ptr + 1
                best = max(cur , new)
                cur = best
        return cur
        