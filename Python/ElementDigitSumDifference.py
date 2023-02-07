# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit_dict = {}
        element_sum = sum(nums)
        digit_sum = 0

        for num in nums:
            temp = num
            digit_dict[num] = []
            while temp > 10:
                r = temp % 10
                digit_dict[num].append(r)
                temp = int(temp/10)
            if temp == 10:
                digit_dict[num].append(1)
            else:
                digit_dict[num].append(temp)
            digit_sum += sum(digit_dict[num])

        return abs(element_sum-digit_sum)
