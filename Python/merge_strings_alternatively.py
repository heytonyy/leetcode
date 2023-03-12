# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        output = ''
        shorter = word1 if len(word1) < len(word2) else word2
        longer = word1 if len(word1) >= len(word2) else word2

        for i in range(len(shorter)):
            output += word1[i] + word2[i]
        
        if i < len(longer):
            output += longer[i+1:]

        return output