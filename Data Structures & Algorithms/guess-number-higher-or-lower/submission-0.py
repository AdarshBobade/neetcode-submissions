# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high :
            my_guess = ( high + low )//2
            ans = guess(my_guess)
            if ans == 0 :
                return my_guess
            elif ans == -1 :
                high = my_guess - 1
            else :
                low = my_guess + 1
        







        