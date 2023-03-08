# https://leetcode.com/problems/pascals-triangle/description/
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        count = 0
        pascals = []
        while count <= numRows:
            if count == 1:
                pascals.append([1])
            if count == 2:
                pascals.append([1,1])
            
            if count > 2:
                last_row = pascals[len(pascals) - 1]
                new_row = [1]
                
                for i in range(len(last_row) - 1):
                    new_row.append(last_row[i] + last_row[i+1])
                
                new_row.append(1)
                pascals.append(new_row)

            count+=1

        return pascals
    
# TESTING 
s = Solution()
print(s.generate(5))

