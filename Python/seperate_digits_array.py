# https://leetcode.com/problems/separate-the-digits-in-an-array/
from typing import List

# list comprehension is sooo good. feels like playing a video game with arrays.
# <3 python

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        output = []
        for num in nums:
            digits = [ int(x) for x in list(str(num)) ]
            output.extend(digits)
        
        return output