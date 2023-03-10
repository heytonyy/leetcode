from typing import List

class Solution:

    def bubble_sort(self, nums: List[int]) -> int:
        '''
        compares two adjacent numbers, largest numbers bubbles to end of array
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] >= nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums
    

    def selection_sort(self, nums: List[int]) -> int:
        '''
        find min values, save index, swap min value with first position, repeat
        until end of list
        '''
        for i in range(len(nums)):
            min_idx = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return nums
    
    def insertion_sort(self, nums: List[int]) -> int:
        '''
        everything left of index ico is in order.
        '''
        for i in range(len(nums)):
            temp = nums[i]
            j = i
            while(j > 0 and temp < nums[j-1]):
                nums[j] = nums[j-1]
                j = j - 1
            nums[j] = temp

        return nums










# TESTING
test_cases = [
    ([1,2,3,4,5], [1,2,3,4,5]),
    ([5,4,3,2,1], [1,2,3,4,5]),
    ([1,2,3,4,5,6], [1,2,3,4,5,6]), 
    ([6,5,4,3,2,1], [1,2,3,4,5,6]),
    ([1,2,3,4,5,6,7], [1,2,3,4,5,6,7]),
    ([7,6,5,4,3,2,1], [1,2,3,4,5,6,7]),
    ([1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8]),
    ([8,7,6,5,4,3,2,1], [1,2,3,4,5,6,7,8]),
    ([1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9]),
]

s = Solution()
for idx, key in enumerate(test_cases):
    test_case = key[0]
    expected = key[1]
    actual = s.insertion_sort(test_case)
    result = "PASSED!" if actual == expected else "FAILED!"
    print(f"Test case {idx+1} - {result}")
    assert actual == expected