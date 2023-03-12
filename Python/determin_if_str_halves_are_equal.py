# https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s)//2
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a = s[:mid]
        b = s[mid:]

        vowels_a = 0
        for x in a:
            if x in vowels:
                vowels_a += 1
        vowels_b = 0
        for x in b:
            if x in vowels:
                vowels_b += 1

        return vowels_a == vowels_b