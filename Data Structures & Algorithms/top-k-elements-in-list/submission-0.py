class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        result = []
        for x in nums:
            freq_dict[x] = freq_dict.get( x , 0) + 1

        buckets = [[] for _ in range(len(nums)+1)]
        for key , val in freq_dict.items():
            buckets[val].append(key)
        
        for i in range( len(buckets) -1 , -1 ,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result









        

        