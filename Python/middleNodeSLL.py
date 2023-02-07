# https://leetcode.com/problems/middle-of-the-linked-list/submissions/892844140/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case
        if not head:
            return None

        # find mid point
        counter = 0
        current = head
        while current:
            counter += 1
            current = current.next
        mid = int(counter/2)
        
        # set the pointer to midnode
        counter = 0
        current = head
        while not counter == mid:
            counter += 1
            current = current.next
        left_pointer = head
        
        return current