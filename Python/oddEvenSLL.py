# https://leetcode.com/problems/odd-even-linked-list/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def print_sll(self, head: Optional[ListNode]) -> str:
        output = ''
        current = head
        while current:
            output += str(current.val) + ', '
            current = current.next
        output = output[0:len(output)-2]
        return output
    
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        
        return head

# test cases
if __name__ == "__main__":
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # create linked list #1
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)


    # print & check linked list #1
    output = Solution().print_sll(head)
    oddEvenList = Solution().oddEvenList(head)
    print(f'#1 Test: [{output}]')
    print(f'OddEvenList: [{Solution().print_sll(oddEvenList)}]')