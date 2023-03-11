# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
from typing import List

'''
remember: you can sorts by multiple parameters with sorted()
include a list with sorting filters with lambda as key like below
'''

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        return sorted(arr, key=lambda x: [bin(x).count('1'), x])