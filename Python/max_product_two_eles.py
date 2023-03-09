# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_val: int = (nums[0]-1) * (nums[1]-1)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                check = (nums[i]-1)*(nums[j]-1)

                if check > max_val:
                    max_val = check
        

        print(max_val)
        return max_val