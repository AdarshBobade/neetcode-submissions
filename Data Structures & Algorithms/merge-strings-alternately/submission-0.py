class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ch = []
        i , j = 0,0
        while i < len(word1) and j < len(word2):
            ch.append(word1[i])
            ch.append(word2[j])
            i += 1
            j += 1
        return ''.join(ch) + word1[i:] + word2[j:]


