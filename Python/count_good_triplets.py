# https://leetcode.com/problems/count-good-triplets/
from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        good_ones = 0

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if not abs(arr[i] - arr[j]) <= a:
                    continue
                
                for k in range(j+1, len(arr)):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        good_ones += 1

        return good_ones