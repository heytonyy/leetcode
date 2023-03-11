# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
from typing import List

'''
og solution:
def replaceElements(self, arr: List[int]) -> List[int]:
    for i in range(len(arr) - 1):
        arr[i] = max(arr[i+1:])
    arr[-1]=-1
    return arr

but i exceded time limit... so had to use pointers, took 1hr extra :(
'''

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        p1, last_num = len(arr) - 2, arr[len(arr) - 1]

        while(p1 >= 0):
            if last_num < arr[p1]:
                last_num, arr[p1] = arr[p1], last_num
                p1-=1
            else:
                for n in range(len(arr[:p1]), -1, -1):
                    if arr[n] < last_num:
                        arr[n] = last_num
                        p1-=1
                    else:
                        last_num, arr[p1] = arr[p1], last_num
                        p1-=1
                        break
                    
        arr[-1] = -1
        return arr