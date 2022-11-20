# https://leetcode.com/problems/integer-to-roman/submissions/

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        if num/1000 >= 1:
            m = int(num/1000)
            roman += 'M'*m
            num = num - 1000*m
        if num/500 >= 1:
            if num/900 >= 1:
                roman += 'CM'
                num = num - 900
            else:
                c = int((num-500)/100)
                roman += f"D{'C'*c}"
                num = num - 500 - 100*c
        if num/100 >= 1:
            if num/400 >= 1:
                roman += 'CD'
                num = num - 400
            else:
                c = int((num)/100)
                roman += f"{'C'*c}"
                num = num - 100*c
        if num/50 >= 1:
            if num/90 >= 1:
                roman += 'XC'
                num = num - 90
            else:
                x = int((num-50)/10)
                roman += f"L{'X'*x}"
                num = num - 50 - 10*x
        if num/10 >= 1:
            if num/40 >= 1:
                roman += 'XL'
                num = num - 40
            else:
                x = int((num)/10)
                roman += f"{'X'*x}"
                num = num - 10*x       
        if num/5 >= 1:
            if num/9 >= 1:
                roman += 'IX'
                num = num - 9
            else:
                i = int((num-5)/1)
                roman += f"V{'I'*i}"
                num = num - 5 - 1*i
        if num/1 >= 1:
            if num/4 >= 1:
                roman += 'IV'
                num = num - 4
            else:
                roman += f"{'I'*num}"
        return roman