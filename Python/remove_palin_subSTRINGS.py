# 

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        def is_palindrome(word):
            return word == word[::-1]
        
        def largest_pali_substr(substrings):
            pali = []
            for s in substrings:
                if is_palindrome(s[0]):
                    pali.append(s)
            lrgst = pali[0]
            for p in pali:
                if len(p[0]) > len(lrgst[0]):
                    lrgst = p
            return lrgst

        count = 0
        while len(s) > 0:
            substrings = [ (s[i:j], (i,j)) for i in range(len(s)) for j in range(i+1, len(s)+1) ]
            _, (p1, p2) = largest_pali_substr(substrings)
            count += 1
            s = s[0:p1] + s[p2:]

        return count