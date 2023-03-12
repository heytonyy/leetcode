# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

class Solution:
    def digitCount(self, num: str) -> bool:

        def letter_counter():
            d = {}
            for n in num:
                if not n in d:
                    d[n]=1
                else:
                    d[n]+=1
            return d

        letter_dict = letter_counter()
        
        for i in range(len(num)):
            if not int(num[i]) == num.count(str(i)):
                return False
            
        return True