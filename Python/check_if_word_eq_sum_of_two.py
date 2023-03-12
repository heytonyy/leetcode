# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/
import string

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        def alpha_num_dict():
            d={}
            count=0
            for letter in string.ascii_lowercase:
                d[letter]=str(count)
                count+=1
            return d

        codex = alpha_num_dict()
        first_nums = second_nums = target_nums = ''
        
        for f in firstWord:
            first_nums += codex[f]
        for s in secondWord:
            second_nums += codex[s]
        for t in targetWord:
            target_nums += codex[t]

        return (int(first_nums) + int(second_nums)) == int(target_nums)