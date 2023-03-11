# https://leetcode.com/problems/maximum-units-on-a-truck/
from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        print(boxTypes)

        loaded = weight = 0
        for i in range(len(boxTypes)):
            if not loaded < truckSize:
                break

            need = truckSize - loaded
            curr_load = boxTypes[i][0]
            curr_weight = boxTypes[i][1]
            if curr_load <= need:
                loaded += curr_load
                weight += curr_weight * curr_load
            else:
                loaded += need
                weight += curr_weight * need
            
        return weight