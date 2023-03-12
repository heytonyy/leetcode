# https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        first_index = word.find(ch)
        if first_index == -1:
            return word

        pre = word[0:first_index + 1]
        post = word[first_index + 1:]
        
        return pre[::-1] + post