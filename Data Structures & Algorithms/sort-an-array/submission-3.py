class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Using Heap sort ->
        def heapify(i , size):
            
            while True :
                largest = i
                l , r = (2*i + 1) , (2*i + 2)
                if l < size and nums[l] > nums[largest] :
                    largest = l
                if r < size and nums[r] > nums[largest] :
                    largest = r
                if largest == i :
                    break
                nums[i] , nums[largest] = nums[largest] , nums[i]
                i = largest
        def build_heap(n):
            
            last_non_leaf = n//2 - 1
            for i in range(last_non_leaf , -1 ,-1):
                heapify(i , n)
            
        s = len(nums)
        build_heap(s)
        while s > 0:
            nums[0] , nums[s-1] = nums[s-1] ,nums[0]
            s -= 1
            heapify(0 , s)
            
        
        return nums







        