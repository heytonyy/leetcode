# https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        from string import ascii_lowercase 
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        abc = list(ascii_lowercase)
        d = dict()
        for idx, letter in enumerate(abc):
            d[letter]=morse[idx]
        transf = []
        for word in words:
            code=""
            for lett in word:
                code += d[lett]
            if code not in transf:
                transf.append(code)
        return len(transf)