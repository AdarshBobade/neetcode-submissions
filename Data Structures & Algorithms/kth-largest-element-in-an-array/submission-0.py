class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def heapify(arr , i):
            size = len(arr)
            while True:
                l , r = (2*i + 1) , (2*i + 2)
                smallest = i
                if l < size and arr[l] < arr[smallest]:
                    smallest = l
                if r < size and arr[r] < arr[smallest] :
                    smallest = r
                if smallest == i:
                    break
                
                arr[i] , arr[smallest] = arr[smallest] , arr[i]
                i = smallest 

        minHeap = nums[:k]
        for i in range(k//2 -1 , -1 ,-1):
            heapify(minHeap , i)

        for i in range(k , len(nums)):
            if minHeap[0] < nums[i] :
                minHeap[0] = nums[i]
                heapify(minHeap , 0)


        return minHeap[0]

        
        