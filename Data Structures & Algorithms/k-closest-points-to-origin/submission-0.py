class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def insert(heap , new_pt, dis):
            heap.append([new_pt , dis])
            i = len(heap) - 1
            while i > 0 and heap[(i-1)//2][-1] < heap[i][-1] :
                heap[i] , heap[(i-1)//2] = heap[(i-1)//2] , heap[i]
                i = (i-1)//2
        
        def delete_max(heap) :
            heap[0] = heap[len(heap) - 1]
            heap.pop()
            heapify(heap , 0)

        def heapify(heap , i):
            size = len(heap)
            while True:
                largest = i
                l , r = (2*i + 1) , (2*i + 2)
                if l < size and heap[l][-1] > heap[largest][-1] :
                    largest = l
                if r < size and heap[r][-1] > heap[largest][-1] :
                    largest = r
                if largest == i :
                    break
                
                heap[i] , heap[largest] = heap[largest] , heap[i]
                i = largest
        
        def build_heap(heap):
            for i in range(len(heap)//2 - 1 , -1 ,-1):
                heapify(heap , i)
        
        minHeap = []
        for i in range(k):
            x , y = points[i]
            dis = x**2 + y **2
            minHeap.append([points[i] ,dis])
        build_heap(minHeap)

        for i in range(k , len(points)):
            x , y = points[i]
            dis = x**2 + y **2
            if dis < minHeap[0][-1] :
                delete_max(heap)
                insert(heap , points[i] , dis)
        
        ans = []
        for i in range(k):
            ans.append(minHeap[i][0])
        return ans









