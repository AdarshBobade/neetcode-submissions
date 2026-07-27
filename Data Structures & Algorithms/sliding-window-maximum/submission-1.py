class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int):
        def heapify(arr, i):
            size = len(arr)
            while True:
                largest = i
                lt, rt = 2 * i + 1, 2 * i + 2

                if lt < size and (
                    arr[lt][0] > arr[largest][0] or
                    (arr[lt][0] == arr[largest][0] and arr[lt][1] > arr[largest][1])
                ):
                    largest = lt

                if rt < size and (
                    arr[rt][0] > arr[largest][0] or
                    (arr[rt][0] == arr[largest][0] and arr[rt][1] > arr[largest][1])
                ):
                    largest = rt

                if largest == i:
                    break

                arr[i], arr[largest] = arr[largest], arr[i]
                i = largest

        def build_heap(arr):
            for i in range(len(arr) // 2 - 1, -1, -1):
                heapify(arr, i)

        def insert(arr, val, idx):
            arr.append([val, idx])
            i = len(arr) - 1

            while i > 0:
                p = (i - 1) // 2
                if (
                    arr[i][0] > arr[p][0] or
                    (arr[i][0] == arr[p][0] and arr[i][1] > arr[p][1])
                ):
                    arr[i], arr[p] = arr[p], arr[i]
                    i = p
                else:
                    break

        def delete_max(arr):
            arr[0] = arr[-1]
            arr.pop()
            if arr:
                heapify(arr, 0)

        maxHeap = []

        for i in range(k):
            maxHeap.append([nums[i], i])

        build_heap(maxHeap)

        res = [maxHeap[0][0]]

        l, r = 1, k

        while r < len(nums):
            insert(maxHeap, nums[r], r)

            while maxHeap and maxHeap[0][1] < l:
                delete_max(maxHeap)

            res.append(maxHeap[0][0])

            l += 1
            r += 1

        return res