class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tmp = 0
        lft_ptr = 0
        rt_ptr = len(s)-1
        while lft_ptr < rt_ptr:
            tmp = s[rt_ptr]
            s[rt_ptr] = s[lft_ptr]
            s[lft_ptr] = tmp
            
            lft_ptr += 1
            rt_ptr -= 1




        