# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d=dict()
        arr=nums
        for n in nums:
          if n in d:
            d[n]+=1
          else:
            d[n]=1
        for i, v in enumerate(nums):
          arr[i]=0
          for (val, count) in d.items():
            if v > val:
              arr[i] += d[val]
        return arr