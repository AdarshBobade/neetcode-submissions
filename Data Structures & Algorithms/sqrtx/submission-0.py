class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        while low <= high:
            root = (high + low)//2
            if root * root == x :
                return root
            elif root * root > x :
                high = root - 1
            else :
                low = root + 1
        return low - 1