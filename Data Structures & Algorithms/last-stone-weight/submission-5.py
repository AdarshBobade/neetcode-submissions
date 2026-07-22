import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        while maxHeap and len(maxHeap) > 1 :
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)
            if abs(x < y) or abs(y < x) :
                heapq.heappush(maxHeap , -abs(x - y))
        return -maxHeap[0] if maxHeap else 0

        