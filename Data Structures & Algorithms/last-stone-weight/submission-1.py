class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def delete_max(heap , i):
            if heap is None :
                return 0
            hv = heap[0]
            last = heap.pop()
            if heap :
                heap[0] = last
                l , r = (2*i + 1) , (2*i + 2)
                while i < len(heap) :
                    if l < len(heap) and heap[l] > heap[i] :
                        heap[i] , heap[l] = heap[l] , heap[i]
                        i = l
                    elif r < len(heap) and heap[r] > heap[i] :
                        heap[i] , heap[r] = heap[r] , heap[i]
                        i = r
                    else :
                        break
            return hv
        
        def insert(arr , val):
            arr.append(val)
            i = len(arr) - 1
            while i > 0 and arr[i] > arr[(i -1 )//2]:
                arr[i] , arr[(i -1 )//2] = arr[(i -1 )//2] , arr[i]
                i = (i-1)//2


        
        def heapify(arr , i):
            size = len(arr)
            while True:
                largest = i
                l , r = (2*i + 1) , (2*i + 2)
                if l < size and arr[l] > arr[largest] :
                    largest = l
                if r < size and arr[r] > arr[largest]:
                    largest = r
                if largest == i :
                    break
                arr[i] , arr[largest] = arr[largest] , arr[i]
                i = largest

        def build_heap(arr):
            for i in range(len(arr)//2 -1 ,-1,-1):
                heapify(arr , i)

        build_heap(stones)
        while stones and len(stones) > 1:
            x = delete_max(stones , 0)
            y = delete_max(stones , 0)
            if x < y or y < x :
                insert(stones , abs(x - y))
        
        return stones[0] if stones else 0
            





        