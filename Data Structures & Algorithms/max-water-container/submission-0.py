class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i , j = 0 , len(heights) - 1
        cur_area = 0
        while i < j :
            breadth = j - i
            if heights[i] <= heights[j]:
                height = heights[i]
                area = height * breadth
                i += 1
            elif heights[i] > heights[j] : 
                height = heights[j]
                area = height * breadth
                j -= 1
            best = max(cur_area , area)
            cur_area = best
        
        return cur_area




        