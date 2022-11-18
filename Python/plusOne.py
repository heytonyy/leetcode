## https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1]+=1
            return digits
        else:
            zeros=0
            for nine in reversed(digits):
                if nine != 9:
                    end = len(digits)-zeros-1
                    digits[end]+=1
                    break
                zeros+=1
            if len(digits) == zeros:
                return [1]+[0]*zeros
            begin = digits[0:end+1]
            return begin+[0]*zeros
            