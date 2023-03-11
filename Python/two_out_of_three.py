# https://leetcode.com/problems/two-out-of-three/submissions/913299637/
from typing import List
from collections import defaultdict

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        d=defaultdict(set)
        for n1 in nums1:
            d[n1].add('nums1')
        for n2 in nums2:
            d[n2].add('nums2')
        for n3 in nums3:
            d[n3].add('nums3')

        return [ key for key in d.keys() if len(d[key]) > 1 ]