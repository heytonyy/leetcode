# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
      totals=list()
      for i in range(len(nums)):
        totals.append(sum(nums[0:i+1]))
      return totals