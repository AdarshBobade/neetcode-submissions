class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack , output = [] , []
        for i in range(len(temperatures) -1 , -1 ,-1):
            if len(stack) == 0:
                stack.append([temperatures[i] , i])
                output.append(0)
                continue
            while stack and stack[-1][0] <= temperatures[i] :
                stack.pop()
            if not stack :
                output.append(0)
            else :
                output.append(stack[-1][-1] - i)
            stack.append([temperatures[i] , i])
        return output[::-1]
                
        