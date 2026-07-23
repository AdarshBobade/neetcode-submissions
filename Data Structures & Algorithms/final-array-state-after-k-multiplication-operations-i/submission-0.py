import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(nums[i], i) for i in range(len(nums))]
        heapq.heapify(heap)

        for _ in range(k):
            value, idx = heapq.heappop(heap)
            value *= multiplier
            nums[idx] = value
            heapq.heappush(heap, (value, idx))

        return nums