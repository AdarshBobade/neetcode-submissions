
# Monotonic Decreasing deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q1 = collections.deque()
        output = []
        l = r = 0
        while r < len(nums):
            while q1 and nums[q1[-1]] < nums[r]:
                q1.pop()
            q1.append(r)

            if q1[0] < l:
                q1.popleft()

            if (r+1) >= k :
                output.append(nums[q1[0]])
                l += 1
            r += 1
        return output

