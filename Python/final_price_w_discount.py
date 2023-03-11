# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        output=[]

        for i in range(len(prices)):
            for j in range(1,len(prices)):
                if j>i and prices[j]<=prices[i]:
                    output.append(prices[i]-prices[j])
                    break
            else:
                output.append(prices[i])
                
        return output