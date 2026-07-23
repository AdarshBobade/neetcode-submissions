import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-x for x in gifts]
        heapq.heapify(maxHeap)
        for _ in range(k):
            num = -heapq.heappop(maxHeap)
            heapq.heappush(maxHeap , -int(num**(1/2)))
        return -sum(maxHeap)


        