# https://leetcode.com/problems/merge-similar-items/
from typing import List

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:

        items1_counter=Counter(dict(items1))
        items2_counter=Counter(dict(items2))
        total_dict=items1_counter + items2_counter
        
        return sorted(total_dict.items())