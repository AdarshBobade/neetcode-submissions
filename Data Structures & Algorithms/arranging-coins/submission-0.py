class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 1
        high = n
        while low <= high :
            mid = ( high + low )//2
            sum_mid = (mid * (mid + 1) )//2
            if sum_mid == n :
                return mid 
            elif sum_mid > n :
                high = mid - 1
            else :
                low = mid + 1
        return high