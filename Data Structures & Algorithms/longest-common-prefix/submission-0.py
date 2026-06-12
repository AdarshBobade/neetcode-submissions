class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       temp = ''
       strs.sort(key=len)
       for i in range(len(strs[0])):
        for s in strs:
            if s[i] != strs[0][i]:
                return temp
        temp+=strs[0][i]
       return temp


       


