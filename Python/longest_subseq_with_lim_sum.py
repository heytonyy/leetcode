# https://leetcode.com/problems/longest-subsequence-with-limited-sum/
from typing import List
from itertools import accumulate
from bisect import bisect_right


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # print(f'Original Nums: {nums}')
        # sorted_nums = sorted(nums)
        # print(f'Sorted: {sorted_nums}')
        # print(f'Queries: {queries}')
        # acc_nums = list(accumulate(sorted_nums))
        # print(f'Accumulate: {acc_nums}')
        # bi_right = [bisect_right(acc_nums,q) for q in queries]
        # print(f'Bisect Right: {bi_right}')
        # return []

        nums = list(accumulate(sorted(nums)))
        return [bisect_right(nums,q) for q in queries]