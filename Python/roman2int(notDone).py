# https://leetcode.com/problems/roman-to-integer/

def romanToInt(s: str) -> int:
    total = 0
    for i in range(len(s)):
        print(s[i])
        if s[i] == 'M':
            total+= 1000
        elif i+1 == len(s):
            if s[i] == 'C' and s[i+1] == 'M':
                total+= 900
        elif s[i] == 'D':
            total+= 500
        elif i+1 < len(s):
            if s[i] == 'C' and s[i+1] == 'D':
                total+= 400
        elif s[i] == 'C':
            total+= 100
        elif i+1 == len(s):
            if s[i] == 'X' and s[i+1] == 'C':
                total+= 90
        elif s[i] == 'L':
            total+= 50
        elif i+1 == len(s):
            if s[i] == 'X' and s[i+1] == 'L':
                total+= 40
        elif s[i] == 'X':
            total+= 10
        elif i+1 == len(s):
            if s[i] == 'I' and s[i+1] == 'X':
                total+= 9
        elif s[i] == 'V':
            total+= 5
        elif i+1 == len(s):
            if s[i] == 'I' and s[i+1] == 'V':
                total+= 4
        elif s[i] == 'I':
            total+=1
        print(total)
    return total

s = "LVIII"

print(romanToInt(s))