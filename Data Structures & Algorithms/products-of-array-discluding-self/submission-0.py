class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]
        postfix = [1]
        output = []

        for i in range(len(nums)):
            prefix.append(nums[i]*prefix[i])
            postfix.append((nums[-i-1])*postfix[i])

        postfix = postfix[::-1]
        for i in range(len(nums)):
            output.append(prefix[i]*postfix[i+1])
        return output

        

                



        
        
        