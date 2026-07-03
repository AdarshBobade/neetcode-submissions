class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)
        ans = 0
        lmax , rmax = 0 , 0
        i , j = 0 , (len(height) - 1)
        while i < len(height) and j > -1 :
            lmax = max(lmax , height[i])
            rmax = max(rmax , height[j])
            left[i] = lmax
            right[j] = rmax
            i += 1
            j -= 1
        for i in range(len(height)-1):
            water = ( min(left[i] , right[i]) - height[i] )
            if water < 0 :
                continue
            else :
                ans += water
        
        return ans
            



            



        
        