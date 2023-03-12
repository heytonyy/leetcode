# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/


class Solution:
    def freqAlphabets(self, s: str) -> str:

        def char_to_digit_dict():
            from string import ascii_lowercase
            alpha = ascii_lowercase
            alpha_num = 1
            d = {}
            for letter in alpha:
                d[str(alpha_num)] = letter
                alpha_num += 1
            return d

        codex = char_to_digit_dict()
        output = ''
        p1 = 0

        while p1 < len(s):
            if p1 + 2 < len(s) and s[p1 + 2] == '#':
                val = s[p1:p1+2]
                p1 += 3
            else:
                val = s[p1]
                p1 += 1
            output += codex[val]

        return output